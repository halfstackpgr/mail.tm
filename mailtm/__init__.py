import typing as t

from .abc.modals import Account, Message, Domain
from enum import Enum


class CacheType(Enum):
    NEW_ACCOUNT = "account"
    OLD_MESSAGE = "old_message"
    NEW_MESSAGE = "new_message"
    DOMAIN = "domain"


class InternalCache:
    def __init__(self) -> None:
        self.internal_memory_map: t.Dict[
            CacheType, t.Union[t.List[Message], t.List[Account], Domain]
        ] = {}

    def __build_cache(self) -> None:
        self.internal_memory_map = {
            CacheType.DOMAIN: [],
            CacheType.NEW_ACCOUNT: [],
            CacheType.NEW_MESSAGE: [],
            CacheType.OLD_MESSAGE: [],
        }

    def __get_cache(
        self, cache_type: CacheType
    ) -> t.Union[t.List[Message], t.List[Account], Domain]:
        return self.internal_memory_map[cache_type]

    def get_old_messages(self) -> t.Optional[t.List[Message]]:
        memory = self.__get_cache(CacheType.OLD_MESSAGE)
        assert isinstance(memory, Message) is True
        return memory
