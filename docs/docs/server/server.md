# Mail Server

This package not only encompasses fundamental SDK functionalities but also integrates an additional layer of scripts tailored specifically for **managing clients** in an **event-driven fashion**, reminiscent of popular frameworks such as discord.py or hikari. By utilizing this SDK, you gain access to a client that seamlessly dispatches events, **enhancing the overall functionality and versatility of your application.**

## Sample Usage:

```python
import mailtm
from mailtm.abc import ServerAuth

server = mailtm.MailServer(
    server_auth=ServerAuth(
        account_id="...",
        account_token="...",
    )
)

@server.on_new_message
async def handle_new_message(event: NewMessage):
    print(event.new_message.text)

server.run()
```
## Understanding the execution

After importing the Server module,

- The mailtm.MailServer creates a server instance to receive new messages.
- The server_auth parameter requires details of the client for initiating API call pooling. *This parameter should be passed with ServerAuth.
- Subsequently, the server's main body is implemented.
- Since this server-like implementation relies solely on event dispatches, two types of decorators are provided to subscribe to any event.
- The `.run()` function is used to execute the server through asynchronous loops.