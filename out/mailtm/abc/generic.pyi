import msgspec

__all__ = ['MessageFrom', 'MessageTo', 'MessageAttachment', 'Token', 'ViewDetails', 'ViewMapping', 'ViewSearch']

class MessageFrom(msgspec.Struct):
    name: str
    address: str

class MessageTo(msgspec.Struct):
    name: str
    address: str

class MessageAttachment(msgspec.Struct):
    id: str
    filename: str
    content_type: str
    disposition: str
    transfer_encoding: str
    related: bool
    size: int
    download_url: str

class Token(msgspec.Struct):
    id: str
    token: str

class ViewDetails(msgspec.Struct):
    first: str
    last: str
    previous: str
    next: str

class ViewMapping(msgspec.Struct):
    variable: str
    property: str
    required: bool

class ViewSearch(msgspec.Struct):
    template: str
    variable_representation: str
    mappings: list[ViewMapping]
