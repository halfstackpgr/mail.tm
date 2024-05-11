"""
Module for events that get triggered in the Mail.tm server.

This module contains a set of classes representing different events that get triggered
in the `Mail.tm` server. These events can be used to create callbacks for when certain
actions happen in the server.

- `NewMessage`: Triggered when a new message is received.
- `MessageDelete`: Triggered when a message is deleted using the server instance.
- `DomainChange`: Triggered when the email domain is changed.
- `AccountSwitched`: Triggered when the account is switched to a different account.
- `NewAccountCreated`: Triggered when a new account is created.
- `AccountDeleted`: Triggered when an account is deleted.
- `ServerStarted`: Triggered when the server is started.
- `ServerCalledOff`: Triggered when the server is ended.

"""

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


from ..impls.xclient import AsyncMail
from ..core.methods import AttachServer
from ..abc.modals import Message, Domain, Account
from ..core.methods import ServerAuth


class BaseEvent:
    """
    Base event for all the concurrent events.
    """

    def __init__(
        self, event: str, client: AsyncMail, _server: AttachServer
    ) -> None:
        self._server = _server
        self.event = event
        self.client = client
        pass


class NewMessage(BaseEvent):
    """
    Event triggered when a message is received.
    """

    def __init__(
        self,
        event: str,
        client: AsyncMail,
        _server: AttachServer,
        new_message: Message,
    ) -> None:
        self.new_message = new_message
        super().__init__(event, client, _server)

    async def delete_message(self) -> None:
        if self.new_message.message_id is not None:
            await self._server.server.dispatch(
                MessageDelete(
                    "MessageDelete",
                    self.client,
                    self.new_message,
                    self._server,
                )
            )
            await self.client.delete_message(self.new_message.message_id)

    async def mark_as_seen(self) -> None:
        if self.new_message.message_id is not None:
            await self.client.mark_as_seen(self.new_message.message_id)


class MessageDelete(BaseEvent):
    """
    Event triggered when a message  gets deleted using the server instance.

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

    def __init__(
        self,
        new_domain: Domain,
        event: str,
        client: AsyncMail,
        _server: AttachServer,
    ) -> None:
        self.new_domain = new_domain
        super().__init__(event, client, _server)


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

    def __init__(
        self, event: str, client: AsyncMail, _server: AttachServer
    ) -> None:
        super().__init__(event, client, _server)


class ServerCalledOff(BaseEvent):
    """
    Event triggered when the server is ended.
    """

    ...
