from ..abc.modals import Account as Account, Domain as Domain, Message as Message
from _typeshed import Incomplete
from enum import Enum

class CacheType(Enum):
    NEW_ACCOUNTS = 'account'
    OLD_MESSAGE = 'old_message'
    NEW_MESSAGE = 'new_message'
    DOMAIN = 'domain'

class InternalCache:
    internal_memory_map: Incomplete
    def __init__(self) -> None: ...
    def build_cache(self) -> None: ...
    def get_old_messages(self) -> list[Message] | None: ...
    def get_new_messages(self) -> list[Message] | None: ...
    def get_new_accounts(self) -> list[Account] | None: ...
    def get_domain_cache(self) -> list[Domain] | None: ...
    def reset_cache(self) -> None: ...
    def add_item_to_cache(self, cache_type: CacheType, item: Message | Account | Domain) -> None: ...
    def get_cache_size(self) -> int: ...
    def clean_cache(self) -> None: ...
