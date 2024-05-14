import msgspec
import typing as t


class MessageFrom(msgspec.Struct):
    """
    Represents a data class containing details of messages.
    """

    name: str = msgspec.field(name="name")
    """
    Name of the `Account` by which the `Message` was sent.
    """
    address: str = msgspec.field(name="address")
    """
    Email address of the `Account` by which the `Message` was sent.
    """


class MessageTo(msgspec.Struct):
    name: str = msgspec.field(name="name")
    """
    Name of the `Account` to which the `Message` was sent.
    """
    address: str = msgspec.field(name="address")
    """
    Email address of the `Account` to which the `Message` was sent.
    """


class MessageAttachment(msgspec.Struct):
    id: str = msgspec.field(name="id")
    """
    ID of the message attachment.
    """
    filename: str = msgspec.field(name="filename")
    """
    The name of the attachment file.
    """
    content_type: str = msgspec.field(name="contentType")
    """
    The MIME type of the attachment.
    """
    disposition: str = msgspec.field(name="disposition")
    """
    The Content-Disposition header of the attachment.
    """
    transfer_encoding: str = msgspec.field(name="transferEncoding")
    """
    The Transfer-Encoding header of the attachment.
    """
    related: bool = msgspec.field(name="related")
    """
    Whether the attachment is related to the main body of the message.
    """
    size: int = msgspec.field(name="size")
    """
    The size of the attachment in bytes.
    """
    download_url: str = msgspec.field(name="downloadUrl")
    """
    The URL where the attachment can be downloaded from.
    """


class Token(msgspec.Struct):
    id: str = msgspec.field(name="id")
    """
    ID of the account.
    """
    token: str = msgspec.field(name="token")
    """
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
    """
    _type: str = msgspec.field(name="@type")
    """
    The type of the view.
    """
    first: str = msgspec.field(name="hydra:first")
    """
    The URL of the first page in the view.
    """
    last: str = msgspec.field(name="hydra:last")
    """
    The URL of the last page in the view.
    """
    previous: str = msgspec.field(name="hydra:previous")
    """
    The URL of the previous page in the view.
    """
    next: str = msgspec.field(name="hydra:next")
    """
    The URL of the next page in the view.
    """


class ViewMapping(msgspec.Struct):
    """
    Struct representing a mapping between a variable and a property.
    """

    _type: str = msgspec.field(name="@type")
    """
    The type of the mapping.
    """
    variable: str = msgspec.field(name="variable")
    """
    The variable of the mapping.
    """
    property: str = msgspec.field(name="property")
    """
    The property of the mapping.
    """
    required: bool = msgspec.field(name="required")
    """
    Whether the mapping is required.
    """


class ViewSearch(msgspec.Struct):
    _type: str = msgspec.field(name="@type")
    """
    The type of the view.
    """

    """
    The type of the view.
    """

    template: str = msgspec.field(name="hydra:template")
    """
    The URL template of the view.
    """

    variable_representation: str = msgspec.field(name="hydra:variableRepresentation")
    """
    The representation of variables in the view.
    """

    mappings: t.List[ViewMapping] = msgspec.field(name="hydra:mapping")
    """
    A list of mappings for the view.
    """
