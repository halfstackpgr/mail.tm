"""
This module contains classes representing different methods available in the Mail.tm webservice.
Each class represents a set of related methods.
"""

from __future__ import annotations

from dataclasses import dataclass
import typing as t

if t.TYPE_CHECKING:
    from mailtm.server.srv import MailServer


@dataclass
class DomainMethods:
    """
    Represents methods related to domains in Mail.tm webservice.
    """

    GET_ALL_DOMAINS = "domains"
    """
    Retrieves all domains.
    """
    GET_DOMAIN_BY_ID = "domains/{id}"
    """
    Retrieves a domain by ID.
    """


@dataclass
class AccountMethods:
    """
    Represents methods related to accounts in Mail.tm webservice.
    """

    CREATE_ACCOUNT = "accounts"
    """
    Creates a new account.
    """
    GET_ACCOUNT_BY_ID = "accounts/{id}"
    """
    Retrieves an account by ID.
    """
    DELETE_ACCOUNT_BY_ID = "accounts/{id}"
    """
    Deletes an account by ID.
    """
    GET_ME = "me"
    """
    Retrieves the current logged in account.
    """

    GET_ACCOUNT_TOKEN = "token"
    """
    Retrieves the token of the account.
    """


@dataclass
class MessageMethods:
    """
    Represents methods related to messages in Mail.tm webservice.
    """

    GET_ALL_MESSAGES = "messages"
    """
    Retrieves all messages.
    """
    GET_MESSAGE_BY_ID = "messages/{id}"
    """
    Retrieves a message by ID.
    """

    DELETE_MESSAGE_BY_ID = "messages/{id}"
    """
    Deletes a message by ID.
    """

    PATCH_MESSAGE_BY_ID = "messages/{id}"
    """
    Updates a message by ID.
    """

    GET_SOURCES_BY_ID = "sources/{id}"

    """
    Retrieves sources for a message by ID.
    """


@dataclass
class ServerAuth:
    """
    A data class to authenticate with the server-client for Server Implementation.
    """

    account_token: str
    """
    The token of the account.
    """
    account_id: str
    """
    The ID of the account.
    """
    account_address: t.Optional[str] = None
    """
    The address of the account.
    """
    account_password: t.Optional[str] = None
    """
    The password of the account."""


@dataclass
class AttachServer:
    server: MailServer
