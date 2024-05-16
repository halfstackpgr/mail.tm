"""
🚀 ABCs for implementation the object oriented SDK.

Includes:

- GenericType
    For the generic type used in the SDK.
- ModalType
    For the modals that are used in interaction with API.
"""

__all__ = ["GenericType", "ModalType"]

from . import generic as GenericType
from . import modals as ModalType
