# Async Mail
Client used for asynchronous operations using the `aiohttp` client library. This would work in sessions.

!!! warn
    After you're finished with a session. Do not forget to close the session yourself by calling `close()`. This will close the session and it won't eat memory any further.

## Base

::: mailtm.impls.xclient
