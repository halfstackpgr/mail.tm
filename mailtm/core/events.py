from ..impls.xclient import AsyncMail
from .methods import AttachServer
from ..abc.modals import Message, Domain, Account
from ..core.methods import ServerAuth


class BaseEvent:
    def __init__(self, event: str, client: AsyncMail, _server: AttachServer) -> None:
        self.__server = _server
        self.event = event
        self.client = client
        pass


class RecieveMessage(BaseEvent):
    """
    Event triggered when a message is recieved.
    """

    def __init__(
        self, event: str, client: AsyncMail, _server: AttachServer, new_message: Message
    ) -> None:
        self.new_message = new_message
        super().__init__(event, client, _server)

    async def delete_message(self) -> None:
        if self.new_message.message_id is not None:
            await self.client.delete_message(self.new_message.message_id)

    async def mark_as_seen(self) -> None:
        if self.new_message.message_id is not None:
            await self.client.mark_as_seen(self.new_message.message_id)


class MessageDelete(BaseEvent):
    """
    Event triggered when a message get's deleted using the server instance.

    `Note`: This won't get triggered if the client is used to delete any message
    """

    def __init__(
        self,
        event: str,
        client: AsyncMail,
        deleted_message: Message,
        _server: AttachServer,
    ) -> None:
        self.deleted_message = deleted_message
        super().__init__(event, client, _server)


class DomainChange(BaseEvent):
    """
    Event triggered when the email domain is changed.
    """

    new_domain: Domain


class AccountSwitched(BaseEvent):
    """
    Event triggered when the account is switched to a different account.
    """

    last_account_auth: ServerAuth
    new_account_auth: ServerAuth


class NewAccountCreated(BaseEvent):
    """
    Event triggered when a new account is created.
    """

    new_account_auth: ServerAuth
    new_account: Account


class AccountDeleted(BaseEvent):
    """
    Event triggered when an account is deleted.
    """

    deleted_account_auth: ServerAuth
    deleted_account: Account


class ServerStarted(BaseEvent):
    """
    Event triggered when the server is started.
    """

    def __init__(self, event: str, client: AsyncMail, _server: AttachServer) -> None:
        super().__init__(event, client, _server)


class ServerEnded:
    """
    Event triggered when the server is ended.
    """
