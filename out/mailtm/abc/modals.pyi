import datetime
import msgspec
from .generic import (
    MessageAttachment as MessageAttachment,
    MessageFrom as MessageFrom,
    MessageTo as MessageTo,
    ViewDetails as ViewDetails,
    ViewSearch as ViewSearch,
)

class Domain(msgspec.Struct):
    id: str | None
    domain_name: str | None
    is_active: bool | None
    is_private: bool | None
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None

class Account(msgspec.Struct):
    id: str | None
    address: str | None
    quota: int | None
    used: int | None
    is_disabled: bool | None
    is_deleted: bool | None
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None

class Message(msgspec.Struct):
    id: str | None
    account_id: str | None
    message_id: str | None
    message_from: MessageFrom | None
    message_to: list[MessageTo] | None
    subject: str | None
    seen: bool | None
    is_deleted: bool | None
    html: list[str] | None
    has_attachments: bool | None
    attachments: list[MessageAttachment] | None
    size: int | None
    downloadUrl: str | None
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    cc: list[str] | None
    bcc: list[str] | None
    flagged: bool | None
    verifications: list[str] | None
    retention_date: datetime.datetime | None
    retention: bool | None
    text: str | None

class Source:
    id: str | None
    download_url: str | None
    data: str | None

class MessagePageView(msgspec.Struct):
    messages: list[Message] | None
    total_items: int | None
    view_search: ViewSearch | None
    view_details: ViewDetails | None

class DomainPageView(msgspec.Struct):
    domains: list[Domain] | None
    total_items: int | None
    view_details: ViewDetails | None
    view_search: ViewSearch | None
