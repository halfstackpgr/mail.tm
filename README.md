![SDK Banner](https://github.com/halfstackpgr/Mail.tm/assets/118044992/67e3a10a-f7d4-44bc-ae11-cd70ad6ee0d3)


<div align="center">
  <h1>Mail.tm</h1>
  <text>Stack Development Kit (Python)</br></text>
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json" alt="Ruff">
    <img src="https://github.com/halfstackpgr/py-codeforces/actions/workflows/python-publish.yml/badge.svg" alt="Passing Package">
    <img src="https://img.shields.io/badge/python-Strict-checking?style=plastic&logo=python&label=Type-Checking&labelColor=yellow" alt="Static Badge">
</div>

>[!INFO]
> Without the documentation it is almost worthless to even start to operate with the library, kindly refer to the [**documentation**](https://halfstackpgr.github.io/Mail.tm/).

## Introduction

Welcome to the Mail.tm Stack Development Kit, designed to enhance your experience with the renowned temporary email service, [Mail.tm](http://mail.tm). Here's why you'll find it indispensable:

1. **Enhanced Integration:** This kit streamlines interactions with Mail.tm's API, empowering you to seamlessly integrate its features into your applications. Whether you're automating email workflows or incorporating temporary email capabilities, this SDK has you covered.

2. **Comprehensive Documentation:** Methods are constructed using the documentation, available [here](http://docs.mail.tm).
   
3. **Adherence to Terms:** Rest assured, this SDK complies fully with Mail.tm's terms of usage, ensuring a seamless and secure experience for both developers and users. By respecting Mail.tm's conditions, we prioritize the integrity and reliability of the service by this kit.

4. **Assurance of safety** This repository prioritizes your safety. With frequent updates to dependencies, we ensure that no vulnerable dependencies compromise your security. Count on us for a secure and reliable experience.

Experience the power and convenience of Mail.tm with our Stack Development Kit – your gateway to efficient and reliable temporary email solutions.

## Key Features:

1. **Versatility at its Core:** Recognizing the diverse needs of users, we've packed this library to cater to various requirements. Whether you're seeking basic data fetching capabilities or integration with sophisticated bots, we've got you covered with two distinct clients and client-less data fetchers.

    - `xclient.AsyncMail`: Utilize this client for asynchronous interactions with the API, leveraging a session for seamless communication. Ideal for asynchronous workflows requiring speed and efficiency.

    - `client.SyncMail`: Opt for this client for synchronous requests to the API, ensuring simplicity and reliability with each interaction. Perfect for synchronous operations demanding consistency.

    - `get` or `xget`: Explore these client-less data fetchers and helpers for streamlined operations without the need for session management. 

        - `xget`: Facilitates asynchronous operations, enhancing performance and responsiveness.
        
        - `get`: Supports synchronous operations, prioritizing simplicity and ease of use.

2. **Type-Safety:** 

   We prioritize strict type-checking throughout the entire codebase of the SDK. You can trust that no type-related errors will interrupt your workflow, ensuring a smooth and error-free experience.

3. **Enhanced Speed:**

   Unlike traditional data validation libraries or Python's built-in `json` module, we leverage [msgspec](https://github.com/jcrist/msgspec) for accelerated data delivery within the codebase. Experience faster performance and streamlined data handling.

## Stellar Feature:

> [!NOTE]
> This script sets up a [**pooling-based**](https://docs.python.org/3/library/multiprocessing.html) server that checks the API every second for new events. When a difference is detected, the corresponding event is dispatched, allowing you to respond dynamically to incoming messages.

In addition to the core SDK functionalities, this package offers an additional layer of scripts designed to handle clients in an event-driven manner, reminiscent of frameworks like `discord.py` or `hikari`. With this SDK, you gain access to a client that dispatches events seamlessly.

Here's a sample usage scenario:

```python
from mailtm.server.events import NewMessage
from mailtm.core.methods import ServerAuth
from mailtm.server.srv import MailServer

# Initialize MailServer with authentication details
server = MailServer(
    server_auth=ServerAuth(
        account_id="...",  # Your account ID.
        account_token="...",  # Your account token.
    )
)

# Define an event handler for new messages
@server.on_new_message 
async def event(event: NewMessage):
    print(event.new_message.text)

# Start the event loop
server.run()
```
This would initiate the event-runner which would start to pool, and a server is then initiated.

### End

