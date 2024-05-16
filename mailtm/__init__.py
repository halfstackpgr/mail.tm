"""
## 📨 Mail.tm Stack Development Kit

Welcome to the Mail.tm Stack Development Kit, designed to enhance your experience with
the renowned temporary email service, [Mail.tm](http://mail.tm). Here's why you'll find
it indispensable:

1. #### Enhanced Integration:
This kit streamlines interactions with Mail.tm's API, empowering you to seamlessly
integrate its features into your applications. Whether you're automating email
workflows or incorporating temporary email capabilities, this SDK has you covered.

2. #### Comprehensive Documentation: Methods are constructed using the documentation,
available [here](http://docs.mail.tm).

3. #### Adherence to Terms:
Rest assured, this SDK complies fully with Mail.tm's terms of usage, ensuring a seamless
and secure experience for both developers and users. By respecting Mail.tm's conditions,
we prioritize the integrity and reliability of the service by this kit.

4. #### Assurance of safety:
This repository prioritizes your safety. With frequent updates to
dependencies, we ensure that no vulnerable dependencies compromise your security. Count on us
for a secure and reliable experience.

Experience the power and convenience of Mail.tm with our Stack Development Kit - your gateway to efficient and reliable temporary email solutions.

---
### Credits:
Created by GitHub: [@halfstackpgr](https://github.com/halfstackpgr)
For any query or bug: [Raise an Issues](https://github.com/halfstackpgr/mailtm/issues)
For further updates visit: [GitHub](https://github.com/halfstackpgr/mailtm)
"""

__version__ = "0.1.0"

__all__ = [
    "MailServer",
    "ServerEvents",
    "GenericTypes",
    "ModalTypes",
    "AsyncMail",
    "SyncMail",
    "xget",
    "get",
    "errors",
    "methods"
]

from .server import events as ServerEvents
from .server.impl import MailServer
from .abc import generic as GenericTypes
from .abc import modals as ModalTypes
from .impls.xclient import AsyncMail
from .impls.client import SyncMail
from .impls.pullers import get, xget
from .core import errors, methods