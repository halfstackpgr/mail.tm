# Choosing the Ideal Client for Your Project

This guide will help you determine which of the three main clients is best suited for your use case.

## 💭 Your Requirements

Based on the specific needs of your project, the library offers three primary clients to choose from:

### 📧 AsyncMail

In scenarios where asynchronous operations are essential, such as developing a Discord bot, the AsyncMail client is ideal.

- 🚀 AsyncMail allows you to execute operations without blocking other tasks, ensuring smooth performance and responsiveness.
- 🚀 This client is perfect for situations where avoiding IO bottlenecks is necessary.

### 📧 SyncMail

**SyncMail** is designed for situations where synchronous operation is preferred or required.

- 🚀 SyncMail provides a straightforward synchronous interface, making it a great choice for users who are more comfortable with synchronous programming paradigms or who do not require the complexity of asynchronous operations.
- 🚀 In SyncMail, operations are executed sequentially, one after the other, rather than concurrently.
- 🚀 This approach can be beneficial in certain contexts where simplicity or ease of understanding is prioritized over performance gains from asynchronous execution.

### 📫 Pullers

Pullers are components within a system that retrieve data or messages from a source in a controlled and efficient manner. 

- 🚀 Pullers typically function by periodically querying a source for new data or messages, pulling them into the system for processing. 
- 🚀 This approach is commonly used in scenarios where the rate of data production varies, or where it is impractical to push data to all consumers simultaneously.
- 🚀 This approach allows users to have complete control over the flow of information in a controlled and efficient manner, without having to establish a dedicated session.

## ⭐ Stellar Feature - Custom MailServer

In addition to the various clients, this SDK offers a standout feature that is not officially supported by the website but has been meticulously reproduced to function seamlessly. This feature involves a **pooling-based** server, which continually monitors the API for new events at one-second intervals. Upon detecting a difference, it dispatches the corresponding event, enabling dynamic responses to incoming messages.

We'll discuss this feature in more detail in the `Server` documentation.
