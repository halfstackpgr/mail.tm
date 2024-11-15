import pathlib
import typing as t
from _typeshed import Incomplete
from mailtm.abc.generic import Token as Token
from mailtm.abc.modals import Domain as Domain, Message as Message
from mailtm.core.methods import (
    AttachServer as AttachServer,
    ServerAuth as ServerAuth,
)
from mailtm.impls.xclient import AsyncMail as AsyncMail
from mailtm.server.cache import (
    CacheType as CacheType,
    InternalCache as InternalCache,
)
from mailtm.server.events import (
    BaseEvent as BaseEvent,
    DomainChange as DomainChange,
    NewMessage as NewMessage,
    ServerCalledOff as ServerCalledOff,
    ServerStarted as ServerStarted,
)

default_banner: Incomplete
ServerSideEvents = t.TypeVar("ServerSideEvents", bound=BaseEvent)

class MailServerBase:
    handlers: Incomplete
    mail_client: Incomplete
    collector: Incomplete
    def __init__(
        self,
        server_auth: ServerAuth,
        pooling_rate: int | None,
        banner: bool | None = True,
        banner_path: pathlib.Path | str | None = ...,
        suppress_errors: bool | None = False,
        enable_logging: bool | None = False,
    ) -> None: ...
    def log(
        self,
        message: str,
        severity: t.Literal["INFO", "WARNING", "ERROR"] = "INFO",
    ) -> None: ...
    def subscribe(
        self, event_type: type[BaseEvent]
    ) -> t.Callable[
        [t.Callable[[ServerSideEvents], t.Awaitable[None]]],
        t.Callable[[ServerSideEvents], t.Awaitable[None]],
    ]: ...
    def on_new_message(
        self, func: t.Callable[[NewMessage], t.Awaitable[None]]
    ): ...
    def on_new_domain(
        self, func: t.Callable[[DomainChange], t.Awaitable[None]]
    ): ...
    async def dispatch(self, event: BaseEvent) -> None: ...
    async def shutdown(self) -> None: ...
    async def runner(self) -> None: ...
    def run(self) -> None: ...
