import typing as t
import asyncio

from mailtm.core.methods import ServerAuth
from mailtm.server.events import ServerEvents
from mailtm.abc.modals import Message, Domain
from mailtm.abc.generic import Token
from mailtm.impls.xclient import AsyncMail

T = t.TypeVar('T', bound=ServerEvents)

class MailServer:
    def __init__(self, server_auth: ServerAuth) -> None:
        self.handlers: t.Dict[
            t.Type[ServerEvents],
            t.List[t.Callable[[ServerEvents], t.Coroutine[t.Any, t.Any, None]]],
        ] = {}
        self._server_auth = server_auth
        self._last_msg: t.List[Message] = []
        self._last_domain: t.List[Domain] = []
        self.mail_client = AsyncMail(
            account_token=Token(
                id=self._server_auth.account_id, token=self._server_auth.account_token
            )
        )

    def subscribe(
        self, event: t.Type[T]
    ) -> t.Callable[
        [t.Callable[[ServerEvents], t.Coroutine[t.Any, t.Any, None]]],
        t.Callable[[ServerEvents], t.Coroutine[t.Any, t.Any, None]],
    ]:
        def decorator(
            func: t.Callable[[ServerEvents], t.Coroutine[t.Any, t.Any, None]],
        ) -> t.Callable[[ServerEvents], t.Coroutine[t.Any, t.Any, None]]:
            if event not in self.handlers:
                self.handlers[event] = []
            self.handlers[event].append(func)
            return func

        return decorator

    async def dispatch(self, event: ServerEvents) -> None:
        if event.__class__ in self.handlers:
            for handler in self.handlers[event.__class__]:
                await handler(event)

    async def runner(self) -> None:
        ###TODO: LOGIC GOES HERE
        pass

    def run(self) -> None:
        asyncio.run(self.runner())
