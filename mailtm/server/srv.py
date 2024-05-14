import typing as t
import asyncio
import aiofiles
import datetime
import pathlib

from colorama import Fore
from mailtm.core.methods import ServerAuth, AttachServer
from mailtm.server.cache import InternalCache, CacheType
from mailtm.server.events import (
    BaseEvent,
    NewMessage,
    DomainChange,
    ServerStarted,
    ServerCalledOff,
)
from mailtm.abc.modals import Message, Domain
from mailtm.abc.generic import Token
from mailtm.impls.xclient import AsyncMail

default_banner = pathlib.Path("mailtm/server/assets/banner.txt")
ServerSideEvents = t.TypeVar("ServerSideEvents", bound=BaseEvent)


class MailServerBase:
    """
    Stellar Addition - Custom MailServer.

    This script sets up a [**pooling-based**](https://docs.python.org/3/library/multiprocessing.html) server
    that checks the API every second for new events. When a difference is detected, the corresponding event
    is dispatched, allowing you to respond dynamically to incoming messages.
    In addition to the core SDK functionalities, this package offers an additional layer of scripts designed
    to handle clients in an event-driven manner, reminiscent of frameworks like `discord.py` or `hikari`. With
    this SDK, you gain access to a client that dispatches events seamlessly.

    Parameters
    ----------
    server_auth : ServerAuth
        The server authentication details.
    pooling_rate : Optional[int]
        The pooling rate in seconds. If not provided, the default pooling rate will be used.
    banner : Optional[bool]
        Whether to display a banner upon initialization. Defaults to True.
    banner_path : Optional[Union[Path, str]]
        The path to the banner file. Defaults to the default banner file.
    suppress_errors : Optional[bool]
        Whether to suppress errors. Defaults to False.
    enable_logging : Optional[bool]
        Whether to enable logging. Defaults to False.

    Example
    -------
    ```python
    import mailtm
    server = mailtm.MailServer(
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
    """

    def __init__(
        self,
        server_auth: ServerAuth,
        pooling_rate: t.Optional[int],
        banner: t.Optional[bool] = True,
        banner_path: t.Optional[t.Union[pathlib.Path, str]] = default_banner,
        suppress_errors: t.Optional[bool] = False,
        enable_logging: t.Optional[bool] = False,
    ) -> None:
        self._banner_enabled = banner
        self._banner_path = banner_path
        self._pooling_rate = pooling_rate
        self._suppress_errors = suppress_errors
        self._logging_enabled = enable_logging
        self.handlers: t.Dict[
            t.Type[BaseEvent],
            list[t.Callable[[BaseEvent], t.Awaitable[None]]],
        ] = {}
        self._server_auth = server_auth
        self._last_msg: list[Message] = []
        self._last_domain: list[Domain] = []
        self.mail_client = AsyncMail(
            account_token=Token(
                id=self._server_auth.account_id,
                token=self._server_auth.account_token,
            )
        )
        self.collector = InternalCache()

    def _extracted_from_on_new_domain_4(self, arg0, func):
        if arg0 not in self.handlers:
            self.handlers[arg0] = []
        self.handlers[arg0].append(func)
        return func

    def log(
        self,
        message: str,
        severity: t.Literal["INFO", "WARNING", "ERROR"] = "INFO",
    ) -> None:
        """
        Logs the message to the console with the corresponding severity.

        Parameters
        ----------
        message : str
            The message to log.
        severity : Literal["INFO", "WARNING", "ERROR"]
            The severity of the message. Defaults to INFO.

        Returns
        -------
        None
        """
        if self._logging_enabled is True:
            current_time = datetime.datetime.now().strftime("%a %m/%d/%Y at %I:%M%p")
            if severity == "INFO":
                print(
                    Fore.LIGHTGREEN_EX + f"[+]{Fore.RESET} On {current_time} " + message
                )
            if self._suppress_errors is False:
                if severity == "WARNING":
                    print(
                        Fore.LIGHTYELLOW_EX
                        + f"[!]{Fore.RESET} On {current_time} "
                        + message
                    )
                elif severity == "ERROR":
                    print(
                        Fore.LIGHTRED_EX
                        + f"[-]{Fore.RESET} On {current_time} "
                        + message
                    )
            else:
                print(
                    Fore.LIGHTWHITE_EX
                    + f"[?] Unrecognized severity: {current_time} "
                    + message
                )

    def subscribe(self, event_type: t.Type[BaseEvent]) -> t.Callable[
        [t.Callable[[ServerSideEvents], t.Awaitable[None]]],
        t.Callable[[ServerSideEvents], t.Awaitable[None]],
    ]:
        """
        Decorator to subscribe a function to handle server events.

        Parameters
        ----------
        event_type : Type[BaseEvent]
            The type of event to subscribe to.

        Returns
        -------
        Callable
            The decorated function.

        Example
        -------
        ```python
        @server.subscribe(ServerSideEvents.NewMessage)
        async def event(event: ServerSideEvents.NewMessage):
            print(event.new_message.text)
        ```
        """

        def decorator(
            handler_func: t.Callable[[ServerSideEvents], t.Awaitable[None]],
        ) -> t.Callable[[ServerSideEvents], t.Awaitable[None]]:
            if event_type not in self.handlers:
                self.handlers[event_type] = []
            self.handlers[event_type].append(handler_func)  # type: ignore
            return handler_func

        return decorator

    def on_new_message(self, func: t.Callable[[NewMessage], t.Awaitable[None]]):
        """
        Registers a callback function to handle new messages.

        Parameters
        ----------
        func : Callable[[NewMessage], Awaitable[None]]
            The callback function to handle new messages.

        Returns
        -------
        The result of the extracted function call.
        """

        return self._extracted_from_on_new_domain_4(NewMessage, func)

    def on_new_domain(self, func: t.Callable[[DomainChange], t.Awaitable[None]]):
        """
        Registers a callback function to handle new domains.

        Parameters
        ----------
        func : Callable[[DomainChange], Awaitable[None]]
            The callback function to handle new domains.

        Returns
        -------
        The result of the extracted function call.
        """
        return self._extracted_from_on_new_domain_4(DomainChange, func)

    async def dispatch(self, event: BaseEvent) -> None:
        """
        Asynchronously dispatches the given event to the appropriate handlers.

        Args:
            self: The MailServerBase instance.
            event (BaseEvent): The event to dispatch.

        Returns:
            None
        """
        for handler in self.handlers.get(type(event), []):
            await handler(event)

    async def _check_for_new_messages(self) -> None:
        """
        Checks for new messages by retrieving message information from the mail client.
        If new messages are detected, triggers a NewMessage event with the new message details.
        """
        msg_view = await self.mail_client.get_messages()
        if (
            msg_view
            and msg_view.messages
            and (not self._last_msg or self._last_msg[0].id != msg_view.messages[0].id)
        ):
            if self._last_msg:
                self._last_msg[0] = msg_view.messages[0]
            else:
                self._last_msg.append(msg_view.messages[0])
            new_message_event = NewMessage(
                "NewMessage",
                client=self.mail_client,
                _server=AttachServer(self),
                new_message=msg_view.messages[0],
            )
            await self.dispatch(new_message_event)
            self.collector.add_item_to_cache(
                CacheType.NEW_MESSAGE, msg_view.messages[0]
            )
            self.log(
                message=f"RECEIVED new message from: {msg_view.messages[0].message_from.address}"  # type: ignore
            )
        return None

    async def _check_for_new_domain(self) -> None:
        """
        Asynchronously checks for a new domain by retrieving domain information from the mail client.
        If a new domain is detected, triggers a DomainChange event with the new domain details.
        """
        domain_view = await self.mail_client.get_domains()
        if (
            domain_view
            and domain_view.domains
            and (
                not self._last_domain
                or self._last_domain[0].id != domain_view.domains[0].id
            )
        ):
            if self._last_domain:
                self._last_domain[0] = domain_view.domains[0]
            else:
                self._last_domain.append(domain_view.domains[0])
            new_domain_event = DomainChange(
                event="DomainChange",
                client=self.mail_client,
                _server=AttachServer(self),
                new_domain=domain_view.domains[0],
            )
            await self.dispatch(new_domain_event)
            self.collector.add_item_to_cache(
                CacheType.NEW_MESSAGE, domain_view.domains[0]
            )
            self.log(
                message=f"Domain Changed: {domain_view.domains[0].domain_name}",
                severity="WARNING",
            )

    async def shutdown(self) -> None:
        """
        Calls the shutdown method on the MailClient instance and dispatches the ServerCalledOff event.

        Returns:
            None
        """
        await self.mail_client.close()
        await self.dispatch(
            ServerCalledOff(
                "Server has been called off",
                self.mail_client,
                AttachServer(server=self),
            )
        )
        self.log(
            message="The mail client session has been called off.",
            severity="WARNING",
        )
        loop = asyncio.get_event_loop()
        loop.stop()
        self.log(
            message="Server shuts down on user's request. Goodbye!",
            severity="WARNING",
        )

    async def _banner(self) -> None:
        """
        Asynchronously prints a banner from the specified file path if it exists.
        The banner is formatted with the current time and date, and includes color codes for different parts of the banner.
        If an exception occurs while reading or printing the banner, it is logged.

        :return: None
        """
        if self._banner_path is not None:
            try:
                async with aiofiles.open(self._banner_path, "r", encoding="utf-8") as f:
                    text = await f.read()
                    details = text.format(
                        time=datetime.datetime.now(),
                        date=f"{datetime.date.today()}",
                        mail=Fore.CYAN,
                        reset=Fore.RESET,
                        sdk=Fore.MAGENTA,
                        ssb=Fore.GREEN,
                        version=Fore.LIGHTBLUE_EX,
                        info=Fore.LIGHTMAGENTA_EX,
                        issues=Fore.RED,
                        warning=Fore.LIGHTYELLOW_EX,
                        dateandtime=Fore.GREEN,
                    )
                    print(details)
            except Exception as e:
                self.log(
                    f"Exception while printing banner:\n{Fore.LIGHTWHITE_EX+str(e)+Fore.RESET}"
                )

    async def runner(self) -> None:
        """
        This function is responsible for executing the main server logic. It starts a session and continuously polls the API for new events. When a difference is detected, the corresponding event is dispatched. The function runs in an infinite loop until it is interrupted by a keyboard interrupt.

        Raises
        ------
            Exception
                If no events have been subscribed to.
        """
        if self._banner_enabled is True:
            await self._banner()
        await self.dispatch(
            ServerStarted("ServerStarted", self.mail_client, AttachServer(self))
        )
        try:
            self.log(
                message="Server-> Session Started: "
                + datetime.datetime.now().strftime("%H:%M:%S")
            )
            self.log(message="Server-> Pooling rate: " + str(self._pooling_rate))
            self.log(message="Server-> Logging enabled: " + str(self._logging_enabled))
            self.log(message="Server-> Banner enabled: " + str(self._banner_enabled))
            self.log(
                message="Server-> Subscribed events: " + str(len(self.handlers.keys()))
            )
            self.log(
                message="Cache initialized. Created 4 maps.",
                severity="WARNING",
            )
            while True:
                await asyncio.sleep(self._pooling_rate or 1)
                if NewMessage in self.handlers:
                    await self._check_for_new_messages()
                if DomainChange in self.handlers:
                    await self._check_for_new_domain()
                if not self.handlers:
                    await self.mail_client.close()
                    raise RuntimeError(
                        "It seems like you have not subscribed to any events."
                    )
        except Exception as e:
            await self.mail_client.close()
            self.log(
                message=f"Exception while running server:\n{Fore.LIGHTWHITE_EX+str(e)+Fore.RESET}"
            )

    def run(self) -> None:
        """
        Executes the main server logic by running the event runner within asyncio event loop.
        """
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.runner())
            loop.close()
        except KeyboardInterrupt:
            asyncio.run(self.shutdown())
