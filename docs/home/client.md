# Choosing the Ideal Client for You

This guide outlines various user cases and client-specific features and methods to help you select the most suitable option.

## Your Requirements

Based on perceived needs, the library accommodates three main cases:

### AsyncMail

In certain scenarios, such as developing a Discord bot, there is a necessity for executing *asynchronous* operations efficiently. 

- For instance, you may want to avoid slowing down operations with IO tasks. 
- To address this concern, the library offers a dedicated client module designed to operate entirely asynchronously, ensuring smooth execution without bottlenecks.

### SyncMail

**SyncMail**, tailored for scenarios where **synchronous operation is preferred or required.** 

- SyncMail offers a synchronous approach for situations where the order of operations or blocking calls are not a concern.
- In SyncMail, operations are carried out sequentially, one after the other, rather than concurrently.
- This can be advantageous in certain contexts where simplicity or ease of understanding is prioritized over performance gains from asynchronous execution. 
- SyncMail provides a straightforward interface for users who are more comfortable with synchronous programming paradigms or who may not require the complexity of asynchronous operations.

### Pullers

Pullers are components within a system designed to retrieve data or messages from a source in a controlled and efficient manner. Unlike traditional push-based communication methods where data is actively pushed to consumers, pull-based systems allow consumers to request data at their own pace, giving them more control over the flow of information.

Pullers typically function by periodically querying a source for new data or messages, pulling them into the system for processing. This approach is commonly used in scenarios where the rate of data production varies, or where it is impractical to push data to all consumers simultaneously.
This approach allows users to basically control the flow of information in a controlled and efficient manner whereever they want to without having to form or make a dedicated session.

## ⭐ Stellar Feature - Custom MailServer

In addition to the various clients, this SDK boasts a standout feature that is not officially supported by the website but has been meticulously reproduced to function seamlessly. This feature involves a **pooling-based** server, which continually monitors the API for new events at one-second intervals. Upon detecting a difference, it dispatches the corresponding event, enabling dynamic responses to incoming messages.

We'd discuss this later in `Server` documentation.

