# Server Events

Events are designed for handling server-related tasks, with a total of 8 events created specifically for this purpose. These events are dispatched to decorators that are subscribed to them.

!!! note
    You are sought to not change or create a custom event, since it still needs to be tested. Without testing, the execution of a custom event might cause problems that server implementations may not be able to deal it causing the server to eventually die.


## Events

::: mailtm.server.events
