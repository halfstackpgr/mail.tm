import requests
import urllib.parse
import msgspec
import typing as t

from ..abc.modals import (
    Account,
    DomainPageView,
    MessagePageView,
    Domain,
    Message,
    Source,
)
from ..abc.generic import Token
from ..core.methods import AccountMethods, DomainMethods, MessageMethods
from ..core.errors import (
    AccountTokenInvalid,
    MissingArgument,
    EntityNotFound,
    MethodNotAllowed,
    RefusedToProcess,
    EntityNotProcessable,
    RatelimitError,
)


class SyncMail:
    def __init__(self, account_token: t.Optional[Token] = None) -> None:
        self._account_token = account_token
        self._base_url = "https://api.mail.tm"
        self._client = requests.Session()
        if self._account_token is not None:
            self._client.headers.update(
                {"Authorization": f"Bearer {self._account_token}"}
            )

    def _interact(
        self,
        method: t.Literal["GET", "POST", "DELETE", "PATCH"],
        url: str,
        body: t.Optional[t.Any] = None,
        params: t.Optional[t.Dict[str, str]] = None,
    ) -> t.Optional[bytes]:
        if method == "GET":
            result = self._client.get(url=url, params=params)
        elif method == "POST":
            result = self._client.post(url=url, json=body)
        elif method == "DELETE":
            result = self._client.delete(url=url, params=params)
        elif method == "PATCH":
            result = self._client.patch(url=url, json=body)
        else:
            raise MethodNotAllowed("Report this as a bug on GitHub")
        if result.status_code == 200:
            return result.content
        elif result.status_code == 400:
            raise MissingArgument(
                "Something in your payload is missing! Or, the payload isn't there at all."
            )
        elif result.status_code == 401:
            raise AccountTokenInvalid(
                "Your token isn't correct (Or the headers hasn't a token at all!). Remember, every request (Except POST /accounts and POST /token) should be authenticated with a Bearer token!"
            )
        elif result.status_code == 404:
            raise EntityNotFound(
                "You're trying to access an account that doesn't exist? Or maybe reading a non-existing message? Go check that!"
            )
        elif result.status_code == 405:
            raise MethodNotAllowed(
                "Maybe you're trying to GET a /token or POST a /messages. Check the path you're trying to make a request to and check if the method is the correct one."
            )
        elif result.status_code == 418:
            raise RefusedToProcess(
                "Server is a teapot. And refused to process your request at the moment. Kindly contact the developers for further details."
            )
        elif result.status_code == 422:
            raise EntityNotProcessable(
                "Some went wrong on your payload. Like, the username of the address while creating the account isn't long enough, or, the account's domain isn't correct. Things like that."
            )
        elif result.status_code == 429:
            raise RatelimitError(
                "You exceeded the limit of 8 requests per second! Try delaying the request by one second!"
            )
        else:
            raise ValueError("Unknown Error")

    def _create_url(self, other_literal: str) -> str:
        return urllib.parse.urljoin(self._base_url, other_literal)

    def get_me(self) -> t.Optional[Account]:
        resp = self._interact(method="GET", url=self._create_url(AccountMethods.GET_ME))
        if resp is not None:
            return msgspec.json.decode(resp, type=Account, strict=False)
        else:
            return None

    def get_domains(self) -> t.Optional[DomainPageView]:
        resp = self._interact(
            method="GET", url=self._create_url(DomainMethods.GET_ALL_DOMAINS)
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=DomainPageView, strict=False)
        else:
            return None

    def get_domain(self, domain_id: str) -> t.Optional[Domain]:
        resp = self._interact(
            method="GET",
            url=self._create_url(DomainMethods.GET_DOMAIN_BY_ID.format(id=domain_id)),
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=Domain, strict=False)
        else:
            return None

    def get_account(self, account_id: str) -> t.Optional[Account]:
        resp = self._interact(
            method="POST",
            url=self._create_url(
                AccountMethods.GET_ACCOUNT_BY_ID.format(id=account_id)
            ),
            params={"id": f"{account_id}"},
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=Account, strict=False)
        else:
            return None

    def create_account(self, address: str, password: str) -> t.Optional[Account]:
        body = {"address": f"{address}", "password": f"{password}"}
        resp = self._interact(
            method="POST",
            url=self._create_url(AccountMethods.CREATE_ACCOUNT),
            body=body,
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=Account, strict=False)
        else:
            return None

    def delete_account(self, account_id: t.Optional[str] = None) -> None:
        if self._account_token is not None and account_id is None:
            self._interact(
                method="DELETE",
                url=self._create_url(
                    AccountMethods.DELETE_ACCOUNT_BY_ID.format(
                        id=self._account_token.id
                    )
                ),
            )
        elif account_id is not None:
            self._interact(
                method="DELETE",
                url=self._create_url(
                    AccountMethods.DELETE_ACCOUNT_BY_ID.format(id=account_id)
                ),
            )
        else:
            raise AccountTokenInvalid("You need an account token to delete an account!")

    def get_messages(self, page: int = 1) -> t.Optional[MessagePageView]:
        parms = {"page": f"{page}"}
        resp = self._interact(
            method="GET",
            url=self._create_url(MessageMethods.GET_ALL_MESSAGES),
            params=parms,
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=MessagePageView, strict=False)
        else:
            return None

    def get_message(self, message_id: str) -> t.Optional[Message]:
        parms = {"id": f"{message_id}"}
        resp = self._interact(
            method="GET",
            url=self._create_url(
                MessageMethods.GET_MESSAGE_BY_ID.format(id=message_id)
            ),
            params=parms,
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=Message, strict=False)
        else:
            return None

    def delete_message(self, message_id: str) -> None:
        parms = {"id": f"{message_id}"}
        self._interact(
            method="DELETE",
            url=self._create_url(
                MessageMethods.DELETE_MESSAGE_BY_ID.format(id=message_id)
            ),
            params=parms,
        )

    def mark_as_seen(self, message_id: str) -> None:
        parms = {"id": f"{message_id}"}
        self._interact(
            method="PATCH",
            url=self._create_url(
                MessageMethods.PATCH_MESSAGE_BY_ID.format(id=message_id)
            ),
            params=parms,
        )

    def get_source(self, source_id: str) -> t.Optional[Source]:
        parms = {"id": f"{source_id}"}
        resp = self._interact(
            method="GET",
            url=self._create_url(MessageMethods.GET_SOURCES_BY_ID.format(id=source_id)),
            params=parms,
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=Source, strict=False)
        else:
            return None
