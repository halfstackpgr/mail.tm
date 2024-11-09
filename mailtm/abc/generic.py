"""
This module provides the following classes for type-safe and msgspec-based handling of the Mail.tm API data types.

- `MessageFrom`: Represents a data class containing details of messages.
- `MessageTo`: Represents a data class containing details of recipients.
- `MessageAttachment`: Represents a data class containing details of attachments.
- `ViewDetails`: Represents a data class containing details of search results.
- `ViewSearch`: Represents a data class containing details of search queries.

These classes are designed to be used with the 'msgspec' library to facilitate quick and efficient data serialization and deserialization.
"""

from __future__ import annotations

__all__ = [
    "MessageFrom",
    "MessageTo",
    "MessageAttachment",
    "Token",
    "ViewDetails",
    "ViewMapping",
    "ViewSearch",
]

import msgspec
import typing as t


class MessageFrom(msgspec.Struct):
    """
    Represents a data class containing details of messages.
    """

    name: str = msgspec.field(name="name")
    """
    Name of the `Account` by which the `Message` was sent.
    
    Returns
    -------
    name : str
        Name of the account message is sent from.
    """
    address: str = msgspec.field(name="address")
    """
    Email address of the `Account` by which the `Message` was sent.
    
    Returns
    -------
    address : str
        Email address of the account message is sent from.
    """


class MessageTo(msgspec.Struct):
    name: str = msgspec.field(name="name")
    """
    Name of the `Account` to which the `Message` was sent.
    
    Returns
    -------
    name : str
        Name of the account message is sent to.
    """
    address: str = msgspec.field(name="address")
    """
    Email address of the `Account` to which the `Message` was sent.
    
    Returns
    -------
    address : str
        Email address of the account message is sent to.
    """


class MessageAttachment(msgspec.Struct):
    id: str = msgspec.field(name="id")
    """
    ID of the message attachment.
    
    Returns
    -------
    id : str
        ID of the message attachment.
    """
    filename: str = msgspec.field(name="filename")
    """
    The name of the attachment file.
    
    Returns
    -------
    filename : str
        The name of the attachment file.
    """
    content_type: str = msgspec.field(name="contentType")
    """
    The MIME type of the attachment.
    
    Returns
    -------
    content_type : str
        The MIME type of the attachment.
    """
    disposition: str = msgspec.field(name="disposition")
    """
    The Content-Disposition header of the attachment.
    
    Returns
    -------
    disposition : str
        The Content-Disposition header of the attachment.
    """
    transfer_encoding: str = msgspec.field(name="transferEncoding")
    """
    The Transfer-Encoding header of the attachment.
    
    Returns
    -------
    transfer_encoding : str
        The Transfer-Encoding header of the attachment.
    """
    related: bool = msgspec.field(name="related")
    """
    Whether the attachment is related to the main body of the message.
    
    Returns
    -------
    related : bool
        Whether the attachment is related to the main body of the message.
    """
    size: int = msgspec.field(name="size")
    """
    The size of the attachment in bytes.
    
    Returns
    -------
    size : int
        The size of the attachment in bytes.
    """
    download_url: str = msgspec.field(name="downloadUrl")
    """
    The URL where the attachment can be downloaded from.
    
    Returns
    -------
    download_url : str
        The URL where the attachment can be downloaded from.
    """


class Token(msgspec.Struct):
    id: str = msgspec.field(name="id")
    """
    ID of the account.
    
    Returns
    -------
    id : str
        ID of the account.
    """
    token: str = msgspec.field(name="token")
    """
    Token of the account.
    
    Returns
    -------
    token : str
        Token of the account.
    """

    def __str__(self) -> str:
        return self.token

    def __repr__(self) -> str:
        return self.__str__()


class ViewDetails(msgspec.Struct):
    """
    Struct representing the details of a view.
    """

    _id: str = msgspec.field(name="@id")
    """
    The unique identifier of the view.
    
    Returns
    -------
    id : str
        The unique identifier of the view.
    """
    _type: str = msgspec.field(name="@type")
    """
    The type of the view.
    
    Returns
    -------
    type : str
        The type of the view.
    """
    first: str = msgspec.field(name="hydra:first")
    """
    The URL of the first page in the view.
    
    Returns
    -------
    first : str
        The URL of the first page in the view.
    """
    last: str = msgspec.field(name="hydra:last")
    """
    The URL of the last page in the view.
    
    Returns
    -------
    last : str
        The URL of the last page in the view.
    """
    previous: str = msgspec.field(name="hydra:previous")
    """
    The URL of the previous page in the view.
    
    Returns
    -------
    previous : str
        The URL of the previous page in the view.
    """
    next: str = msgspec.field(name="hydra:next")
    """
    The URL of the next page in the view.
    
    Returns
    -------
    next : str
        The URL of the next page in the view.
    """


class ViewMapping(msgspec.Struct):
    """
    Struct representing a mapping between a variable and a property.
    """

    _type: str = msgspec.field(name="@type")
    """
    The type of the mapping.
    
    Returns
    -------
    type : str
        The type of the mapping.
    """
    variable: str = msgspec.field(name="variable")
    """
    The variable of the mapping.
    
    Returns
    -------
    variable : str
        The variable of the mapping.
    """
    property: str = msgspec.field(name="property")
    """
    The property of the mapping.
    
    Returns
    -------
    property : str
        The property of the mapping.
    """
    required: bool = msgspec.field(name="required")
    """
    Whether the mapping is required.
    
    Returns
    -------
    required : bool
        Whether the mapping is required.
    """


class ViewSearch(msgspec.Struct):
    """
    A view search system.
    """

    _type: str = msgspec.field(name="@type")
    """
    The type of the view.
    
    Returns
    -------
    type : str
        The type of the view.
    """

    template: str = msgspec.field(name="hydra:template")
    """
    The URL template of the view.
    
    Returns
    -------
    template : str
        The URL template of the view.
    """

    variable_representation: str = msgspec.field(
        name="hydra:variableRepresentation"
    )
    """
    The representation of variables in the view.
    
    Returns
    -------
    variable_representation : str
        The representation of variables in the view.
    """

    mappings: t.List[ViewMapping] = msgspec.field(name="hydra:mapping")
    """
    A list of mappings for the view.
    
    Returns
    -------
    mappings : List[ViewMapping]
        A list of mappings for the view.
    """

    def __str__(self) -> str:
        return self.template

    def __repr__(self) -> str:
        return self.__str__()
