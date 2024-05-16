"""
🚀 This package not only encompasses fundamental SDK functionalities but also integrates an additional 
layer of scripts tailored specifically for managing clients in an event-driven fashion, reminiscent of 
popular frameworks such as discord.py or hikari. By utilizing this SDK, you gain access to a client that 
seamlessly dispatches events, enhancing the overall functionality and versatility of your application.

Includes:

- ⚡ Mail Server
- ⚡ Server Events
"""

__all__ = ["MailServer", "ServerEvents"]

from .impl import MailServer
from . import events as ServerEvents