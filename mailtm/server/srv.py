import typing as t
import asyncio

from mailtm.core.methods import ServerAuth
from mailtm.server.events import BaseEvent, NewMessage, AttachServer
from mailtm.abc.modals import Message, Domain
from mailtm.abc.generic import Token
from mailtm.impls.xclient import AsyncMail

EventT = t.TypeVar(name="EventT", bound=BaseEvent)


class MailServer:
    def __init__(self, server_auth: ServerAuth) -> None:
        self.handlers: t.Dict[
            t.Type[BaseEvent],
            list[t.Callable[[BaseEvent], t.Awaitable[None]]],
        ] = {}
        self._server_auth = server_auth
        self._last_msg: list[Message] = []
        self._last_domain: list[Domain] = []
        self.mail_client = AsyncMail(
            account_token=Token(
                id=self._server_auth.account_id, token=self._server_auth.account_token
            )
        )

    def on_new_message(self, func: t.Callable[[NewMessage], t.Awaitable[None]]):
        if NewMessage not in self.handlers:
            self.handlers[NewMessage] = []
        self.handlers[NewMessage].append(func)  # type: ignore
        return func

    async def dispatch(self, event: BaseEvent) -> None:
        for handler in self.handlers.get(type(event), []):
            await handler(event)

    async def _check_for_new_messages(self) -> t.Optional[Message]:
        msg_view = await self.mail_client.get_messages()
        if msg_view and msg_view.messages:
            if not self._last_msg or self._last_msg[0].id != msg_view.messages[0].id:
                if self._last_msg:
                    self._last_msg[0] = msg_view.messages[0]
                else:
                    self._last_msg.append(msg_view.messages[0])
                new_message_event = NewMessage(
                    "NewMessage",
                    client=self.mail_client,
                    _server=AttachServer(self),
                    new_message=msg_view.messages[0],
                )
                await self.dispatch(new_message_event)
                return msg_view.messages[0]
        return None

    async def runner(self) -> None:
        try:
            print("Runner started...")
            while True:
                await asyncio.sleep(1)
                await self._check_for_new_messages()
        except Exception as e:
            print(f"Error in runner: {e}")
            
            
    def run(self):
        print("Running server...")
        
        asyncio.run(self.runner())
