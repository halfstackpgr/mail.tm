import typing as t
import asyncio

from ..core.methods import ServerAuth
from .events import ServerEvents
from ..abc.modals import Message, Domain
from ..abc.generic import Token
from ..impls.xclient import AsyncMail


class MailServer:
    def __init__(self, server_auth: ServerAuth) -> None:
        self.handlers: t.Dict[t.Type[ServerEvents], t.List[t.Callable[[ServerEvents], None]]] = {}
        self._server_auth = server_auth
        self._last_msg: t.List[Message] = []
        self._last_domain: t.List[Domain] = []
        self.mail_client = AsyncMail(
            account_token=Token(
                id=self._server_auth.account_id, token=self._server_auth.account_token
            )
        )


    
    def subscribe(self, event: t.Type[ServerEvents]) -> t.Callable[[t.Callable[[ServerEvents], None]], t.Callable[[ServerEvents], None]]:
        def decorator(func: t.Callable[[ServerEvents], None]) -> t.Callable[[ServerEvents], None]:
            if event not in self.handlers:
                self.handlers[event] = []
            self.handlers[event].append(func)
            return func
        return decorator

    def dispatch(self, event: ServerEvents) -> None:
        if event.__class__ in self.handlers:
            for handler in self.handlers[event.__class__]:
                handler(event)

    async def runner(self) -> None:
        pass
    
    def run(self) -> None:
        asyncio.run(self.runner())