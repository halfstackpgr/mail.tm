from pathlib import Path
from mailtm.server.srv import default_banner
from .srv import MailServerBase
from ..core.methods import AttachServer, ServerAuth
from ..abc.modals import Account
from ..impls.pullers import xget
import typing as t
from .events import (
    NewAccountCreated,
    DomainChange,
    NewMessage,
    MessageDelete,
    AccountSwitched,
    AccountDeleted,
    ServerStarted,
    ServerCalledOff,
)


class MailServer(MailServerBase):
    """
    Stellar Addition - Custom MailServer.
    ---
    This script sets up a [**pooling-based**](https://docs.python.org/3/library/multiprocessing.html) server
    that checks the API every second for new events. When a difference is detected, the corresponding event
    is dispatched, allowing you to respond dynamically to incoming messages.
    In addition to the core SDK functionalities, this package offers an additional layer of scripts designed
    to handle clients in an event-driven manner, reminiscent of frameworks like `discord.py` or `hikari`. With
    this SDK, you gain access to a client that dispatches events seamlessly.

    Here's a sample usage scenario:

    ```python
    server = MailServer(
        server_auth=ServerAuth(
            account_id="...",  # Your account ID.
            account_token="...",  # Your account token.
        )
    )
    # Define an event handler for new messages
    # The stand-alone decorators should be used
    # without the brackets since we provide no
    # function to handle, and append with the
    # handler.
    @server.on_new_message
    async def event(event: NewMessage):
        print(event.new_message.text)
    # Start the event loop
    server.run()
    ```
    This would initiate the event-runner which would start to pool, and a server is then initiated.

    """

    ...

    def __init__(
        self,
        server_auth: ServerAuth,
        pooling_rate: int | None,
        banner: bool | None = True,
        banner_path: Path | str | None = default_banner,
        suppress_errors: bool | None = False,
        enable_logging: bool | None = False,
    ) -> None:
        self.pull = xget()
        self.collector: t.Dict[str, str] = {}
        super().__init__(
            server_auth,
            pooling_rate,
            banner,
            banner_path,
            suppress_errors,
            enable_logging,
        )

    async def cache(self):
        def get_created_accounts(
            account_id: str,
        ) -> t.Optional[t.List[Account]]: ...

    async def create_account(
        self, account_address: str, account_password: str
    ) -> t.Optional[Account]:
        """
        Asynchronously creates a new account with the given email address and password.

        Args:
            account_address (str): The email address of the new account.
            account_password (str): The password for the new account.

        Returns:
            Optional[Account]: The newly created account object if successful, None otherwise.

        Raises:
            Exception: If there is an error creating the account.

        """
        try:
            new_account = await self.mail_client.create_account(
                account_address, account_password
            )
            token = await self.pull.get_account_token(
                account_address, account_password
            )
            if token is not None and new_account is not None:
                account_auth = ServerAuth(
                    account_token=token.token,
                    account_id=token.id,
                    account_address=account_address,
                    account_password=account_password,
                )
                await self.dispatch(
                    NewAccountCreated(
                        new_account=new_account,
                        new_account_auth=account_auth,
                        event="NewAccountCreated",
                        client=self.mail_client,
                        _server=AttachServer(self),
                    )
                )
                return new_account
        except Exception as e:
            self.log(
                message="Could not create account: " + str(e), severity="ERROR"
            )

    async def shutdown(self) -> None:
        await self.dispatch(
            ServerCalledOff(
                "ServerCalledOff", self.mail_client, AttachServer(self)
            )
        )
        return await super().shutdown()

    async def runner(self) -> None:
        await self.dispatch(
            ServerStarted(
                "ServerStarted", self.mail_client, AttachServer(self)
            )
        )
        return await super().runner()
