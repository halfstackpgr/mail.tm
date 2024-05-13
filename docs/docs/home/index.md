# 📧 Introduction to SDK

Welcome to the Mail.tm Stack Development Kit, designed to enhance your experience with
the renowned temporary email service, [Mail.tm](http://mail.tm). Here's why you'll find
it indispensable:

## Enhanced Integration
This kit streamlines interactions with Mail.tm's API, empowering you to seamlessly
integrate its features into your applications. Whether you're automating email
workflows or incorporating temporary email capabilities, this SDK has you covered.

- The library provides a way to reduce the memory load. 
- It uses hashmaps for caching the data required to compare and dispatch data related events. 
- The live system works on a routed method of pooling with API which makes it easy to interact with client.

## Comprehensive Documentation
Methods are constructed using the documentation,
available [here](http://docs.mail.tm).
The whole documentation is relying on what the API documentation is, apart from the attributes an instance of any JSON object represents.
Rather than manually spliiting the data and then patching their values under a class, this library directly uses Structs, to do it. 
>Similar to an example class like this all the objects, that is, the `abc`s are made in this library.
```python
class Account(x.Struct):
    account_id: Optional[str]
    another_field: Optional[str]
    some_more_field: Optional[str]
```

>Although the documentation has it's own essential importance. >The docstrings do contain all the necessary information one >would need to know about.

## Adherence to Terms
Rest assured, this SDK complies fully with Mail.tm's terms of usage, ensuring a seamless
and secure experience for both developers and users. By respecting Mail.tm's conditions,
we prioritize the integrity and reliability of the service by this kit.

## Assurance of safety
This repository prioritizes your safety. With frequent updates to
dependencies, we ensure that no vulnerable dependencies compromise your security. Count on us
for a secure and reliable experience.

Experience the power and convenience of Mail.tm with our Stack Development Kit - your gateway to efficient and reliable temporary email solutions.