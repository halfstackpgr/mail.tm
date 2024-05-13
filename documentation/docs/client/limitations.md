# Limitations of the server implmentation.

Well, since the server implementation is not documented in the official documentation of Mail.tm, and is a locally made feature underlying the SDK, it is bound to be having certain limitations along with it.

## Ratelimiting

Handling rate-limit errors manually is currently necessary since predicting the exact timing of these errors is challenging. However, we're considering developing a more efficient method to manage rate limits, especially when making multiple API calls for event monitoring.

## Random Crashes

Mail.tm currently lacks support for providing advance notification of service denial before implementing temporary downtime. Consequently, predicting when the server might randomly go offline is not feasible.

## Not really real-time

While the current implementation involves calling the API every second to monitor for changes, it's important to note that the API response consistently experiences a delay. On average, new messages are detected approximately 20 seconds after their arrival on the mail.tm website. **Thus, the system's real-time capabilities are somewhat limited due to this delay.**