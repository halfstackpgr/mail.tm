from .abc import generic as GenericTypes, modals as ModalTypes
from .core import errors as errors, methods as methods
from .impls.client import SyncMail as SyncMail
from .impls.pullers import get as get, xget as xget
from .impls.xclient import AsyncMail as AsyncMail
from .server import events as ServerEvents
from .server.impl import MailServer as MailServer

__all__ = ['MailServer', 'ServerEvents', 'GenericTypes', 'ModalTypes', 'AsyncMail', 'SyncMail', 'xget', 'get', 'errors', 'methods']
