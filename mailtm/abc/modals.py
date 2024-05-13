import msgspec
import datetime
import typing as t


from .generic import (
    MessageFrom,
    MessageTo,
    MessageAttachment,
    ViewDetails,
    ViewSearch,
)


class Domain(msgspec.Struct):
    _id: t.Optional[str] = msgspec.field(name="@id", default=None)
    """
    `Secrative`: ID of the interaction.
    """

    _type: t.Optional[str] = msgspec.field(name="@type", default=None)
    """
    `Secrative`: Type of the interaction.
    """

    _context: t.Optional[str] = msgspec.field(name="@context", default=None)
    """
    `Secrative`: Context of the interaction.
    """

    id: t.Optional[str] = msgspec.field(name="id", default=None)
    """
    `Not documented`: ID of the interaction.
    """
    domain_name: t.Optional[str] = msgspec.field(name="domain", default=None)
    """
    Name of the domain provided by mail.tm

    Example: @gmail.com, @goster.com
    """
    is_active: t.Optional[bool] = msgspec.field(name="isActive", default=None)
    """
    If the domain is still active.
    """

    is_private: t.Optional[bool] = msgspec.field(name="isPrivate", default=None)
    """
    If the domain is private. Private domains are not visible to the public.
    """
    created_at: t.Optional[datetime.datetime] = msgspec.field(
        name="createdAt", default=None
    )
    """
    The datetime object of creation date of the domain.
    """

    updated_at: t.Optional[datetime.datetime] = msgspec.field(
        name="updatedAt", default=None
    )
    """
    The datetime object of update date of the domain from the latest point of reference.
    """


class Account(msgspec.Struct):
    _id: t.Optional[str] = msgspec.field(name="@id", default=None)
    """
    `Secrative`: ID of the account.
    """

    _type: t.Optional[str] = msgspec.field(name="@type", default=None)
    """
    `Secrative`: Type of the account.
    """

    _context: t.Optional[str] = msgspec.field(name="@context", default=None)
    """
    `Secrative`: Context of the account.
    """

    id: t.Optional[str] = msgspec.field(name="id", default=None)
    """
    `Not documented`: ID of the account.
    """

    address: t.Optional[str] = msgspec.field(name="address", default=None)
    """
    Email address of the account.
    """

    quota: t.Optional[int] = msgspec.field(name="quota", default=None)
    """
    The quota of the account.
    """

    used: t.Optional[int] = msgspec.field(name="used", default=None)
    """
    The amount of quota used by the account.
    """

    is_disabled: t.Optional[bool] = msgspec.field(name="isDisabled", default=None)
    """
    If the account is disabled.
    """

    is_deleted: t.Optional[bool] = msgspec.field(name="isDeleted", default=None)
    """
    If the account is deleted.
    """

    created_at: t.Optional[datetime.datetime] = msgspec.field(
        name="createdAt", default=None
    )
    """
    The datetime object of creation date of the account.
    """

    updated_at: t.Optional[datetime.datetime] = msgspec.field(
        name="updatedAt", default=None
    )
    """
    The datetime object of update date of the account from the latest point of reference.
    """


class Message(msgspec.Struct):
    _id: t.Optional[str] = msgspec.field(name="@id", default=None)
    """
    `Secrative`: ID of the message.
    """

    _type: t.Optional[str] = msgspec.field(name="@type", default=None)
    """
    `Secrative`: Type of the message.
    """

    _context: t.Optional[str] = msgspec.field(name="@context", default=None)
    """
    `Secrative`: Context of the message.
    """

    id: t.Optional[str] = msgspec.field(name="id", default=None)
    """
    ID of the message.
    """

    account_id: t.Optional[str] = msgspec.field(name="accountId", default=None)
    """
    ID of the account to which the message belongs.
    """

    message_id: t.Optional[str] = msgspec.field(name="msgid", default=None)
    """
    Message ID.
    """

    message_from: t.Optional[MessageFrom] = msgspec.field(name="from", default=None)
    """
    Details of the sender of the message.
    """

    message_to: t.Optional[t.List[MessageTo]] = msgspec.field(name="to", default=None)
    """
    Details of the recipients of the message.
    """

    subject: t.Optional[str] = msgspec.field(name="subject", default=None)
    """
    Subject of the message.
    """

    seen: t.Optional[bool] = msgspec.field(name="seen", default=None)
    """
    If the message has been seen by the recipient.
    """

    is_deleted: t.Optional[bool] = msgspec.field(name="isDeleted", default=None)
    """
    If the message is deleted.
    """

    html: t.Optional[t.List[str]] = msgspec.field(name="html", default=None)
    """
    HTML content of the message.
    """

    has_attachments: t.Optional[bool] = msgspec.field(
        name="hasAttachments", default=None
    )
    """
    If the message has attachments.
    """

    attachments: t.Optional[t.List[MessageAttachment]] = msgspec.field(
        name="attachments", default=None
    )
    """
    Attachments associated with the message.
    """

    size: t.Optional[int] = msgspec.field(name="size", default=None)
    """
    Size of the message in bytes.
    """

    downloadUrl: t.Optional[str] = msgspec.field(name="downloadUrl", default=None)
    """
    URL to download the message.
    """

    created_at: t.Optional[datetime.datetime] = msgspec.field(
        name="createdAt", default=None
    )
    """
    Date and time of creation of the message.
    """

    updated_at: t.Optional[datetime.datetime] = msgspec.field(
        name="updatedAt", default=None
    )
    """
    Date and time of last update of the message.
    """

    cc: t.Optional[t.List[str]] = msgspec.field(name="cc", default=None)
    """
    Carbon Copy (CC) recipients of the message.
    """

    bcc: t.Optional[t.List[str]] = msgspec.field(name="bcc", default=None)
    """
    Blind Carbon Copy (BCC) recipients of the message.
    """

    flagged: t.Optional[bool] = msgspec.field(name="flagged", default=None)
    """
    If the message is flagged by the recipient.
    """

    verifications: t.Optional[t.List[str]] = msgspec.field(
        name="verifications", default=None
    )
    """
    Verifications associated with the message.
    """

    retention_date: t.Optional[datetime.datetime] = msgspec.field(
        name="retentionDate", default=None
    )
    """
    Date of retention for the message.
    """

    retention: t.Optional[bool] = msgspec.field(name="retention", default=None)
    """
    If the message is subject to retention.
    """

    text: t.Optional[str] = msgspec.field(name="text", default=None)
    """
    Plain text content of the message.
    """


class Source:
    _id: t.Optional[str] = msgspec.field(name="@id", default=None)
    """
    `Secrative`: ID of the source.
    """

    _type: t.Optional[str] = msgspec.field(name="@type", default=None)
    """
    `Secrative`: Type of the source.
    """

    _context: t.Optional[str] = msgspec.field(name="@context", default=None)
    """
    `Secrative`: Context of the source.
    """

    id: t.Optional[str] = msgspec.field(name="id", default=None)
    """
    The id attribute of the Source.
    """

    download_url: t.Optional[str] = msgspec.field(name="downloadUrl", default=None)
    """
    The download URL attribute of the Source.
    """

    data: t.Optional[str] = msgspec.field(name="data", default=None)
    """
    The data attribute of the Source.
    """


class MessagePageView(msgspec.Struct):
    """
    Page view for messages under a page.
    """

    messages: t.Optional[t.List[Message]] = msgspec.field(
        name="hydra:member", default=None
    )
    """
    List of messages in the view.
    """

    total_items: t.Optional[int] = msgspec.field(name="hydra:totalItems", default=None)
    """
    Total number of items in the view.
    """

    view_search: t.Optional[ViewSearch] = msgspec.field(
        name="hydra:search", default=None
    )
    """
    Search parameters of the view.
    """

    view_details: t.Optional[ViewDetails] = msgspec.field(
        name="hydra:view", default=None
    )
    """
    Details of the view.
    """


class DomainPageView(msgspec.Struct):
    """
    Page view for domains under a page.
    """

    domains: t.Optional[t.List[Domain]] = msgspec.field(
        name="hydra:member", default=None
    )
    """
    List of domains in the view.
    """

    total_items: t.Optional[int] = msgspec.field(name="hydra:totalItems", default=None)
    """
    Total number of domains in the view.
    """

    view_details: t.Optional[ViewDetails] = msgspec.field(
        name="hydra:view", default=None
    )
    """
    Details of the domain view.
    """

    view_search: t.Optional[ViewSearch] = msgspec.field(
        name="hydra:search", default=None
    )
    """
    Search parameters of the domain view.
    """
