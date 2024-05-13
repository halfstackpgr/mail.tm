# Mail Server implementation

??? question "Should we reconsider our implementation method to align with the webhooks approach detailed in the documentation at [mail.tm](https://docs.mail.tm/#listen-to-messages)"
    Given the documentation at [mail.tm](https://docs.mail.tm/#listen-to-messages),
    I've explored the possibility of implementing webhooks for our project. However,
    
    - It appears that the webhooks utilize SSE (Server-Sent Events) instead of conventional webhook captures for real-time event updates.
    - Unfortunately, due to the absence of reliable SSE client implementations in Python, the current implementation stands as the most suitable approach for now.


## Mail Server Base Implementation
!!! note 
    Just below this text, lies the Base implementation of MailServer. You should never use this to create a MailServer instance directly. Instead you should choose MailServer

::: mailtm.server.srv

## The Mail Server

::: mailtm.server.impl