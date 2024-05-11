from .srv import MailServerBase
from ..core.methods import AttachServer
from .events import (
    NewAccountCreated,
    DomainChange,
    NewMessage,
    MessageDelete, 
    AccountSwitched, 
    AccountDeleted,
    ServerStarted,
    ServerCalledOff
)


class MailServer(MailServerBase):
    """
    Stellar Addition - Custom MailServer.
    ---
    This script sets up a [**pooling-based**](https://docs.python.org/3/library/multiprocessing.html) server
    that checks the API every second for new events. When a difference is detected, the corresponding event 
    is dispatched, allowing you to respond dynamically to incoming messages.
    In addition to the core SDK functionalities, this package offers an additional layer of scripts designed 
    to handle clients in an event-driven manner, reminiscent of frameworks like `discord.py` or `hikari`. With
    this SDK, you gain access to a client that dispatches events seamlessly.

    Here's a sample usage scenario:

    ```python
    server = MailServer(
        server_auth=ServerAuth(
            account_id="...",  # Your account ID.
            account_token="...",  # Your account token.
        )
    )
    # Define an event handler for new messages
    # The stand-alone decorators should be used
    # without the brackets since we provide no 
    # function to handle, and append with the 
    # handler.
    @server.on_new_message 
    async def event(event: NewMessage):
        print(event.new_message.text)
    # Start the event loop
    server.run()
    ```
    This would initiate the event-runner which would start to pool, and a server is then initiated.
    
    """
    ...
    
    async def shutdown(self) -> None:
        return await super().shutdown()
    
    async def runner(self) -> None:
        await self.dispatch(ServerStarted("ServerStarted", self.mail_client, AttachServer(self)))
        return await super().runner()