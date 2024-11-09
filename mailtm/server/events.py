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
    Represents a set of Discord UI components attached to a message.

    Parameters
    ----------
    event : str
        A string attached to the BaseEvent that represents the event.
    client : AsyncMail
        An instance AsyncMail that represents the client. You can use this to operate the interactions with the AsyncClient

    _server: AttachServer
        This is not supposed to be used by the user. This attaches a server instance to dispatch events within from events.
    """

    def __init__(
        self, event: str, client: AsyncMail, _server: AttachServer
    ) -> None:
        self._server = _server
        self._event = event
        self._client = client

    @property
    def client(self) -> AsyncMail:
        """
        Client attached to the server context.

        Returns
        -------
        AsyncMail
            an instance of AsyncMail attached to the server in the context of the interaction.
        """
        return self._client

    @property
    def server(self) -> AttachServer:
        """
        An instance of AttachServer, which basically has the MailServer attached to it.

        Returns
        -------
        AttachServer
            an instance of AttachServer, which can be used like `AttachServer.server`. This contains `MailServer`.
        """
        return self._server

    @property
    def event(self) -> str:
        """
        The event string associated with the dispatched class.

        Returns
        -------
        str
            The event string associated with the dispatched class
        """
        return self._event


class NewMessage(BaseEvent):
    """
    Event triggered when a message is received.

    Parameters
    ----------
    new_message : Message
        The message that was received.
    """

    def __init__(
        self,
        event: str,
        client: AsyncMail,
        _server: AttachServer,
        new_message: Message,
    ) -> None:
        self._new_message = new_message
        super().__init__(event, client, _server)

    @property
    def new_message(self) -> Message:
        """
        The new message that was received from the server.

        Returns
        -------
        Message
            An instance of Message which includes the details about message received from the server.
        """
        return self.new_message

    async def delete_message(self) -> None:
        """
        Delete the message from the Mail Box.
        """
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
        """
        Flag the message as seen.
        """
        if self.new_message.message_id is not None:
            await self.client.mark_as_seen(self.new_message.message_id)


class MessageDelete(BaseEvent):
    """
    Event triggered when a message  gets deleted using the server instance.
    Note: This won't get triggered if the client is used to delete any message

    Parameters
    ----------
    deleted_message : Message
        The message that was deleted.
    """

    def __init__(
        self,
        event: str,
        client: AsyncMail,
        deleted_message: Message,
        _server: AttachServer,
    ) -> None:
        self._deleted_message = deleted_message
        super().__init__(event, client, _server)

    @property
    def deleted_message(self) -> Message:
        """
        The message that was deleted.

        Returns
        -------
        Message
            The message that was deleted.
        """
        return self._deleted_message


class DomainChange(BaseEvent):
    """
    Event triggered when the email domain is changed.

    Parameter
    ---------
    new_domain : Domain
        The new domain that was set.
    """

    def __init__(
        self,
        new_domain: Domain,
        event: str,
        client: AsyncMail,
        _server: AttachServer,
    ) -> None:
        self._new_domain = new_domain
        super().__init__(event, client, _server)

    @property
    def new_domain(self) -> Domain:
        """
        The domain that got changed.

        Returns
        -------
        Domain
            A domain that was changed
        """
        return self._new_domain


class AccountSwitched(BaseEvent):
    """
    Event triggered when the account is switched to a different account.

    Parameter
    ---------
    last_account_auth: ServerAuth
        An instance of ServerAuth that represents the last account.

    """

    def __init__(
        self,
        event: str,
        client: AsyncMail,
        _server: AttachServer,
        last_account_auth: ServerAuth,
    ) -> None:
        self._last_account_auth = last_account_auth
        super().__init__(event, client, _server)

    @property
    def last_account_auth(self) -> ServerAuth:
        """
        Get the ServerAuth of the last account.

        Returns:
        --------
        ServerAuth
            An instance of ServerAuth that represents the last account.
        """
        return self.last_account_auth


class NewAccountCreated(BaseEvent):
    """
    Event triggered when a new account is created.

    Parameters
    ----------
    new_account_auth: ServerAuth
        An instance of ServerAuth that represents the new account.

    new_account: Account
        An instance of Account that represents the new account.
    """

    def __init__(
        self,
        new_account_auth: ServerAuth,
        new_account: Account,
        event: str,
        client: AsyncMail,
        _server: AttachServer,
    ) -> None:
        self._new_account_aut = new_account_auth
        self._new_account = new_account
        super().__init__(event, client, _server)

    @property
    def new_account_auth(self) -> ServerAuth:
        """
        The server authentication related to the new account.

        Returns
        -------
        ServerAuth:
            An instance representing the details used in server authentication.
        """
        return self._new_account_aut

    @property
    def new_account(self) -> Account:
        """
        The new account that was created.

        Returns
        -------
        Account
            An instance of Account that represents the new account.
        """
        return self._new_account


class AccountDeleted(BaseEvent):
    """
    Event triggered when an account is deleted.
    """

    def __init__(
        self, event: str, client: AsyncMail, _server: AttachServer
    ) -> None:
        super().__init__(event, client, _server)


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

    def __init__(
        self, event: str, client: AsyncMail, _server: AttachServer
    ) -> None:
        super().__init__(event, client, _server)
