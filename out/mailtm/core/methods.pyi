from dataclasses import dataclass
from mailtm.server.srv import MailServerBase

__all__ = [
    "DomainMethods",
    "AccountMethods",
    "MessageMethods",
    "ServerAuth",
    "AttachServer",
]

@dataclass
class DomainMethods:
    GET_ALL_DOMAINS = ...
    GET_DOMAIN_BY_ID = ...

@dataclass
class AccountMethods:
    CREATE_ACCOUNT = ...
    GET_ACCOUNT_BY_ID = ...
    DELETE_ACCOUNT_BY_ID = ...
    GET_ME = ...
    GET_ACCOUNT_TOKEN = ...

@dataclass
class MessageMethods:
    GET_ALL_MESSAGES = ...
    GET_MESSAGE_BY_ID = ...
    DELETE_MESSAGE_BY_ID = ...
    PATCH_MESSAGE_BY_ID = ...
    GET_SOURCES_BY_ID = ...

@dataclass
class ServerAuth:
    account_token: str
    account_id: str
    account_address: str | None = ...
    account_password: str | None = ...
    def __init__(
        self,
        account_token,
        account_id,
        account_address=...,
        account_password=...,
    ) -> None: ...

@dataclass
class AttachServer:
    server: MailServerBase
    def __init__(self, server) -> None: ...