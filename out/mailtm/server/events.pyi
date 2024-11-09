from ..abc.modals import Account, Domain, Message
from ..core.methods import AttachServer, ServerAuth
from ..impls.xclient import AsyncMail

__all__ = [
    "NewMessage",
    "MessageDelete",
    "DomainChange",
    "AccountSwitched",
    "NewAccountCreated",
    "AccountDeleted",
    "ServerStarted",
    "ServerCalledOff",
]

class BaseEvent:
    def __init__(
        self, event: str, client: AsyncMail, _server: AttachServer
    ) -> None: ...
    @property
    def client(self) -> AsyncMail: ...
    @property
    def server(self) -> AttachServer: ...
    @property
    def event(self) -> str: ...

class NewMessage(BaseEvent):
    def __init__(
        self,
        event: str,
        client: AsyncMail,
        _server: AttachServer,
        new_message: Message,
    ) -> None: ...
    @property
    def new_message(self) -> Message: ...
    async def delete_message(self) -> None: ...
    async def mark_as_seen(self) -> None: ...

class MessageDelete(BaseEvent):
    def __init__(
        self,
        event: str,
        client: AsyncMail,
        deleted_message: Message,
        _server: AttachServer,
    ) -> None: ...
    @property
    def deleted_message(self) -> Message: ...

class DomainChange(BaseEvent):
    def __init__(
        self,
        new_domain: Domain,
        event: str,
        client: AsyncMail,
        _server: AttachServer,
    ) -> None: ...
    @property
    def new_domain(self) -> Domain: ...

class AccountSwitched(BaseEvent):
    def __init__(
        self,
        event: str,
        client: AsyncMail,
        _server: AttachServer,
        last_account_auth: ServerAuth,
    ) -> None: ...
    @property
    def last_account_auth(self) -> ServerAuth: ...

class NewAccountCreated(BaseEvent):
    def __init__(
        self,
        new_account_auth: ServerAuth,
        new_account: Account,
        event: str,
        client: AsyncMail,
        _server: AttachServer,
    ) -> None: ...
    @property
    def new_account_auth(self) -> ServerAuth: ...
    @property
    def new_account(self) -> Account: ...

class AccountDeleted(BaseEvent):
    def __init__(
        self, event: str, client: AsyncMail, _server: AttachServer
    ) -> None: ...

class ServerStarted(BaseEvent):
    def __init__(
        self, event: str, client: AsyncMail, _server: AttachServer
    ) -> None: ...

class ServerCalledOff(BaseEvent):
    def __init__(
        self, event: str, client: AsyncMail, _server: AttachServer
    ) -> None: ...
