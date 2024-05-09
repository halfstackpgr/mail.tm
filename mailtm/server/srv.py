import typing as t
import asyncio
import aiofiles
import datetime
import pathlib

from colorama import Fore
from mailtm.core.methods import ServerAuth, AttachServer
from mailtm.server.events import BaseEvent, NewMessage
from mailtm.abc.modals import Message, Domain
from mailtm.abc.generic import Token
from mailtm.impls.xclient import AsyncMail

default_banner = pathlib.Path("mailtm/server/assets/banner.txt")


class MailServer:
    def __init__(
        self,
        server_auth: ServerAuth,
        pooling_rate: t.Optional[int],
        banner: t.Optional[bool] = True,
        banner_path: t.Optional[t.Union[pathlib.Path, str]] = default_banner,
        suppress_errors: t.Optional[bool] = False,
        enable_logging: t.Optional[bool] = False,
        save_output: t.Optional[bool] = False,
    ) -> None:
        self._banner_enabled = banner
        self._banner_path = banner_path
        self._pooling_rate = pooling_rate
        self._suppress_errors = suppress_errors
        self._logging_enabled = enable_logging
        self._save_output = save_output
        self.handlers: t.Dict[
            t.Type[BaseEvent],
            list[t.Callable[[BaseEvent], t.Awaitable[None]]],
        ] = {}
        self._server_auth = server_auth
        self._last_msg: list[Message] = []
        self._last_domain: list[Domain] = []
        self.mail_client = AsyncMail(
            account_token=Token(
                id=self._server_auth.account_id,
                token=self._server_auth.account_token,
            )
        )

    def on_new_message(
        self, func: t.Callable[[NewMessage], t.Awaitable[None]]
    ):
        if NewMessage not in self.handlers:
            self.handlers[NewMessage] = []
        self.handlers[NewMessage].append(func)  # type: ignore
        return func

    async def dispatch(self, event: BaseEvent) -> None:
        for handler in self.handlers.get(type(event), []):
            await handler(event)

    async def _check_for_new_messages(self) -> t.Optional[Message]:
        print("Checked For New Message: ")
        msg_view = await self.mail_client.get_messages()
        if msg_view and msg_view.messages:
            if (
                not self._last_msg
                or self._last_msg[0].id != msg_view.messages[0].id
            ):
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

    async def _banner(self) -> None:
        if self._banner_path is not None:
            try:
                async with aiofiles.open(
                    self._banner_path, "r", encoding="utf-8"
                ) as f:
                    text = await f.read()
                    details = text.format(
                        time=datetime.datetime.now(),
                        date=f"{datetime.date.today()}",
                        mail=Fore.CYAN,
                        reset=Fore.RESET,
                        sdk=Fore.MAGENTA,
                        ssb=Fore.GREEN,
                        version=Fore.LIGHTBLUE_EX,
                        info=Fore.LIGHTMAGENTA_EX,
                        issues=Fore.RED,
                        warning=Fore.LIGHTYELLOW_EX,
                        dateandtime=Fore.GREEN,
                    )
                    print(details)
            except Exception as e:
                print("Exception while printing banner:\n", e)

    async def save_output(self, content: str) -> None:
        async with aiofiles.open("output.txt", "w+", encoding="utf-8") as f:
            await f.write(f"\nAt time: {datetime.datetime.now()}\n{content}")

    async def runner(self) -> None:
        if self._banner_enabled is True:
            await self._banner()
        while True:
            await asyncio.sleep(self._pooling_rate or 1)
            await self._check_for_new_messages()

    def run(self):
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.runner())
            loop.close()
        except Exception as e:
            print("Exception while running server:\n", e)

