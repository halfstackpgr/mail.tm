import pathlib
import typing as t

from .events import (
    NewAccountCreated,
    MessageDelete,
    AccountSwitched,
    AccountDeleted,
)
from .srv import MailServerBase, default_banner
from .cache import CacheType

from ..core.methods import AttachServer, ServerAuth
from ..abc.modals import Account
from ..abc.generic import Token
from ..impls.pullers import xget


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
        banner_path: pathlib.Path | str | None = default_banner,
        suppress_errors: bool | None = False,
        enable_logging: bool | None = False,
    ) -> None:
        self.pull = xget()
        super().__init__(
            server_auth,
            pooling_rate,
            banner,
            banner_path,
            suppress_errors,
            enable_logging,
        )

    async def create_account(
        self, account_address: str, account_password: str
    ) -> t.Optional[Account]:
        """
        Creates a new account with the given email address and password.

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
            token = await self.pull.get_account_token(account_address, account_password)
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
                        event="A new account got created.",
                        client=self.mail_client,
                        _server=AttachServer(self),
                    )
                )
                self.collector.add_item_to_cache(
                    cache_type=CacheType.NEW_ACCOUNTS, item=new_account
                )
            return new_account
        except Exception as e:
            self.log(message="Could not create account: " + str(e), severity="ERROR")
            return None

    async def delete_message(self, message_id: str) -> None:
        message = await self.mail_client.get_message(message_id=message_id)
        if message:
            try:
                await self.mail_client.delete_message(message_id)
                await self.dispatch(
                    MessageDelete(
                        "Deleted a message.",
                        deleted_message=message,
                        client=self.mail_client,
                        _server=AttachServer(self),
                    )
                )
                self.collector.add_item_to_cache(
                    cache_type=CacheType.OLD_MESSAGE, item=message
                )
            except Exception as e:
                self.log(
                    message="Could not delete message: " + str(e),
                    severity="ERROR",
                )
                return None

    async def switch_account(self, new_account_token: t.Union[Token, str]) -> None:
        try:
            if isinstance(new_account_token, Token):
                self.mail_client._client.headers.update(
                    {"Authorization": f"Bearer {new_account_token.token}"}
                )
                self.log(
                    message=f"Switched to new account with ID: {new_account_token.id}",
                    severity="WARNING",
                )
            if isinstance(new_account_token, str):
                self.mail_client._client.headers.update(
                    {"Authorization": f"Bearer {new_account_token}"}
                )
                self.log(
                    message=f"Switched to new account with Token: {new_account_token}",
                    severity="WARNING",
                )

            await self.dispatch(
                AccountSwitched(
                    event="Account switched",
                    client=self.mail_client,
                    _server=AttachServer(self),
                )
            )

        except Exception as e:
            self.log(message="Could not switch account: " + str(e), severity="ERROR")

    async def delete_account(self, account_id: str) -> None:
        try:
            await self.mail_client.delete_account(account_id)
            self.log(message="Deleted account with ID: " + account_id)
            await self.dispatch(
                AccountDeleted(
                    event=f"Account has been deleted with the ID: {account_id}",
                    client=self.mail_client,
                    _server=AttachServer(self),
                )
            )
        except Exception as e:
            self.log(message="Could not delete account: " + str(e), severity="ERROR")

    async def shutdown(self) -> None:
        self.collector.clean_cache()
        return await super().shutdown()

    async def runner(self) -> None:
        self.collector.build_cache()
        return await super().runner()
