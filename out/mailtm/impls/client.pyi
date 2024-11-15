from ..abc.generic import Token
from ..abc.modals import (
    Account,
    Domain,
    DomainPageView,
    Message,
    MessagePageView,
    Source,
)

__all__ = ["SyncMail"]

class SyncMail:
    def __init__(self, account_token: Token | None = None) -> None: ...
    def get_me(self) -> Account | None: ...
    def get_domains(self) -> DomainPageView | None: ...
    def get_domain(self, domain_id: str) -> Domain | None: ...
    def get_account(self, account_id: str) -> Account | None: ...
    def create_account(
        self, address: str, password: str
    ) -> Account | None: ...
    def delete_account(self, account_id: str | None = None) -> None: ...
    def get_messages(self, page: int = 1) -> MessagePageView | None: ...
    def get_message(self, message_id: str) -> Message | None: ...
    def delete_message(self, message_id: str) -> None: ...
    def mark_as_seen(self, message_id: str) -> None: ...
    def get_source(self, source_id: str) -> Source | None: ...
