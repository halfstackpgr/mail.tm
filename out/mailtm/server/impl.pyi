import pathlib
from ..abc.generic import Token as Token
from ..abc.modals import Account as Account
from ..core.methods import (
    AttachServer as AttachServer,
    ServerAuth as ServerAuth,
)
from ..impls.pullers import xget as xget
from .cache import CacheType as CacheType
from .events import (
    AccountDeleted as AccountDeleted,
    AccountSwitched as AccountSwitched,
    MessageDelete as MessageDelete,
    NewAccountCreated as NewAccountCreated,
)
from .srv import (
    MailServerBase as MailServerBase,
    default_banner as default_banner,
)
from _typeshed import Incomplete

class MailServer(MailServerBase):
    pull: Incomplete
    def __init__(
        self,
        server_auth: ServerAuth,
        pooling_rate: int | None,
        banner: bool | None = True,
        banner_path: pathlib.Path | str | None = ...,
        suppress_errors: bool | None = False,
        enable_logging: bool | None = False,
    ) -> None: ...
    async def create_account(
        self, account_address: str, account_password: str
    ) -> Account | None: ...
    async def delete_message(self, message_id: str) -> None: ...
    async def switch_account(self, new_account_token: Token | str) -> None: ...
    async def delete_account(self, account_id: str) -> None: ...
    async def shutdown(self) -> None: ...
    async def runner(self) -> None: ...
