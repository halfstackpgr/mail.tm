import sys
import typing as t
from enum import Enum

from ..abc.modals import Account, Message, Domain


class CacheType(Enum):
    """
    Class that represents different cache data-types.
    """

    NEW_ACCOUNTS = "account"
    """
    All the new accounts that have been cached ever since the server started.
    `mail_client` operations are never cached.
    """
    OLD_MESSAGE = "old_message"
    """
    All the old messages that have been cached ever since the server started.
    `mail_client` operations are never cached.
    """
    NEW_MESSAGE = "new_message"
    """
    All the new messages that have been cached ever since the server started.
    `mail_client` operations are never cached.
    """
    DOMAIN = "domain"
    """
    All the domain changes that have taken place.
    """


class InternalCache:
    """
    A class to manage an internal cache for different types of data.
    """

    def __init__(self) -> None:
        self.internal_memory_map: t.Dict[
            CacheType,
            t.Union[t.List[Message], t.List[Account], t.List[Domain]],
        ] = {}

    def build_cache(self) -> None:
        """
        Builds the initial cache structure with empty lists for different cache types.
        """
        self.internal_memory_map.update(
            {
                CacheType.DOMAIN: [],
                CacheType.NEW_ACCOUNTS: [],
                CacheType.NEW_MESSAGE: [],
                CacheType.OLD_MESSAGE: [],
            }
        )

    def get_old_messages(self) -> t.Optional[t.List[Message]]:
        """
        Retrieves a list of old messages from the cache.

        Returns:
            Optional[List[Message]]: A list of old messages if available, or None if no old messages are found.
        """

        retunable_list: t.List[Message] = []
        base = self.internal_memory_map.get(CacheType.OLD_MESSAGE)
        if base is None:
            return None
        for item in base:
            if isinstance(item, Message):
                retunable_list.append(item)
        return retunable_list

    def get_new_messages(self) -> t.Optional[t.List[Message]]:
        """
        Retrieves a list of new messages from the cache.

        Returns:
            Optional[List[Message]]: A list of new messages if available, or None if no new messages are found.
        """

        retunable_list: t.List[Message] = []
        base = self.internal_memory_map.get(CacheType.NEW_MESSAGE)
        if base is None:
            return None
        for item in base:
            if isinstance(item, Message):
                retunable_list.append(item)
        return retunable_list

    def get_new_accounts(self) -> t.Optional[t.List[Account]]:
        """
        Retrieves a list of new accounts from the cache.

        Returns:
            Optional[List[Account]]: A list of new accounts if available, or None if no new accounts are found.
        """

        retunable_list: t.List[Account] = []
        base = self.internal_memory_map.get(CacheType.NEW_ACCOUNTS)
        if base is None:
            return None
        for item in base:
            if isinstance(item, Account):
                retunable_list.append(item)
        return retunable_list

    def get_domain_cache(self) -> t.Optional[t.List[Domain]]:
        """
        Retrieves the domain cache from the internal memory map.

        Returns:
            Optional[List[Domain]]: A list of domains if the cache is available,
            otherwise None.
        """

        retunable_list: t.List[Domain] = []
        base = self.internal_memory_map.get(CacheType.DOMAIN)
        if base is None:
            return None
        for item in base:
            if isinstance(item, Domain):
                retunable_list.append(item)
        return retunable_list

    def reset_cache(self) -> None:
        """
        Resets the internal cache of the InternalCache object.

        This function clears all the existing data in the internal memory map of the InternalCache object and replaces it with empty lists for each CacheType.

        Returns:
            None
        """
        self.internal_memory_map = {
            CacheType.DOMAIN: [],
            CacheType.NEW_ACCOUNTS: [],
            CacheType.NEW_MESSAGE: [],
            CacheType.OLD_MESSAGE: [],
        }

    def add_item_to_cache(
        self, cache_type: CacheType, item: t.Union[Message, Account, Domain]
    ) -> None:
        """
        Adds an item to the internal cache of the InternalCache object.

        Args:
            cache_type (CacheType): The type of cache to add the item to.
            item (Union[Message, Account, Domain]): The item to add to the cache.

        Returns:
            None
        """
        self.internal_memory_map[cache_type].append(item)  # type: ignore

    def get_cache_size(self) -> int:
        """
        Get the size of the internal cache.

        Returns:
            int: The size of the internal cache.
        """
        return sys.getsizeof(self.internal_memory_map)

    def clean_cache(self):
        """
        Cleans the cache by removing all data except for domain cache.
        """

        self.internal_memory_map = {}
