"""
🚀 Implementations for clients and pullers.

These includes:
- `clients` - `AsyncMail` for asychronous operations and `SyncMail` for synchronous operations.
- `pullers` - Pullers are components within a system that retrieve data or messages from a source in a controlled and efficient manner.
"""

__all__ = ["AsyncMail", "SyncMail", "xget", "get"]

from .client import SyncMail
from .xclient import AsyncMail
from .pullers import get, xget
