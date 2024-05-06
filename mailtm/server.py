import asyncio
import typing as t


from .abc.generic import Token
from .abc.modals import Message, Domain
from .impls.xclient import AsyncMail
from .core.methods import ServerAuth
from .core.events import RecieveMessage, DomainChange


EventTypes = t.Union[RecieveMessage, DomainChange]

DecoratorType = t.Callable[
    [t.Callable[[EventTypes], None]], t.Callable[[EventTypes], None]
]


class MailServer:
    def __init__(self, server_auth: ServerAuth) -> None:
        self.handlers: t.Dict[
            t.Type[EventTypes], t.List[t.Callable[[EventTypes], None]]
        ] = {}
        self._server_auth = server_auth
        self._last_msg: t.List[Message] = []
        self._last_domain: t.List[Domain] = []
        self.mail_client = AsyncMail(
            account_token=Token(
                id=self._server_auth.account_id, token=self._server_auth.account_token
            )
        )

    def subscribe(self, event: t.Type[EventTypes]):
        def decorator(func):
            if event not in self.handlers:
                self.handlers[event] = []
            self.handlers[event].append(func)
            return func

        return decorator

    def dispatch(self, event: EventTypes):
        if event.__class__ in self.handlers:
            for handler in self.handlers[event.__class__]:
                handler(event)

    def run() -> None:
        pass
