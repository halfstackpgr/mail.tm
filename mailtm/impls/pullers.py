import requests
import aiohttp
import msgspec
import typing as t
import urllib.parse
from ..abc.generic import Token
from ..abc.modals import Account, Domain, DomainPageView
from ..core.methods import AccountMethods, DomainMethods
from ..core.errors import (
    AccountTokenInvalid,
    MissingArgument,
    EntityNotFound,
    MethodNotAllowed,
    RefusedToProcess,
    EntityNotProcessable,
    RatelimitError,
)


class get:
    """
    `Synchronous` : Out-of-client methods  to get, post, delete, and patch data through aiohttp.
    """

    def __init__(self) -> None:
        self._base_url = "https://api.mail.tm"

    def _interact(
        self,
        method: t.Literal["GET", "POST", "DELETE", "PATCH"],
        url: str,
        body: t.Optional[t.Any] = None,
        params: t.Optional[t.Dict[str, str]] = None,
    ) -> t.Optional[bytes]:
        if method not in ["GET", "POST", "DELETE", "PATCH"]:
            raise ValueError("Invalid HTTP method")

        if method == "GET":
            resp = requests.get(url=url, params=params, json=body)
        elif method == "POST":
            resp = requests.post(url=url, params=params, json=body)
        elif method == "DELETE":
            resp = requests.delete(url=url, params=params, json=body)
        elif method == "PATCH":
            resp = requests.patch(url=url, params=params, json=body)

        if resp.status_code == 200:
            return resp.content
        elif resp.status_code == 400:
            raise MissingArgument(
                "Something in your payload is missing! Or, the payload isn't there at all."
            )
        elif resp.status_code == 401:
            raise AccountTokenInvalid(
                "Your token isn't correct (Or the headers hasn't a token at all!). Remember, every request (Except POST /accounts and POST /token) should be authenticated with a Bearer token!"
            )
        elif resp.status_code == 404:
            raise EntityNotFound(
                "You're trying to access an account that doesn't exist? Or maybe reading a non-existing message? Go check that!"
            )
        elif resp.status_code == 405:
            raise MethodNotAllowed(
                "Maybe you're trying to GET a /token or POST a /messages. Check the path you're trying to make a request to and check if the method is the correct one."
            )
        elif resp.status_code == 418:
            raise RefusedToProcess(
                "Server is a teapot. And refused to process your request at the moment. Kindly contact the developers for further details."
            )
        elif resp.status_code == 422:
            raise EntityNotProcessable(
                "Some went wrong on your payload. Like, the username of the address while creating the account isn't long enough, or, the account's domain isn't correct. Things like that."
            )
        elif resp.status_code == 429:
            raise RatelimitError(
                "You exceeded the limit of 8 requests per second! Try delaying the request by one second!"
            )
        else:
            raise ValueError(f"Unknown Error\n TB:\n{resp.text}")

    def create_account(self, address: str, password: str) -> t.Optional[Account]:
        body = {"address": f"{address}", "password": f"{password}"}
        resp = self._interact(
            method="POST",
            url=urllib.parse.urljoin(self._base_url, AccountMethods.CREATE_ACCOUNT),
            body=body,
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=Account, strict=False)
        else:
            return None

    def get_account(self, account_id: str) -> t.Optional[Account]:
        resp = self._interact(
            method="POST",
            url=urllib.parse.urljoin(
                self._base_url,
                AccountMethods.GET_ACCOUNT_BY_ID.format(id=f"{account_id}"),
            ),
            params={"id": f"{account_id}"},
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=Account, strict=False)
        else:
            return None

    def delete_account(self, account_id: str) -> bool:
        resp = requests.delete(
            url=urllib.parse.urljoin(
                self._base_url,
                AccountMethods.DELETE_ACCOUNT_BY_ID.format(id=f"{account_id}"),
            ),
            params={"id": f"{account_id}"},
        )
        if resp.status_code == 204:
            return True
        else:
            return False

    def get_account_token(
        self, account_address: str, account_password: str
    ) -> t.Optional[Token]:
        body = {"address": f"{account_address}", "password": f"{account_password}"}
        resp = self._interact(
            method="POST",
            url=urllib.parse.urljoin(self._base_url, AccountMethods.GET_ACCOUNT_TOKEN),
            body=body,
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=Token, strict=False)
        else:
            return None

    def get_domain(self, domain_id: str) -> t.Optional[Domain]:
        resp = self._interact(
            method="GET",
            url=urllib.parse.urljoin(
                self._base_url, DomainMethods.GET_DOMAIN_BY_ID.format(id=f"{domain_id}")
            ),
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=Domain, strict=False)
        else:
            return None

    def get_domains(self) -> t.Optional[DomainPageView]:
        resp = self._interact(
            method="GET",
            url=urllib.parse.urljoin(self._base_url, DomainMethods.GET_ALL_DOMAINS),
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=DomainPageView, strict=False)
        else:
            return None


class xget:
    """
    `Asynchronous` : Out-of-client methods  to get, post, delete, and patch data through aiohttp.
    """

    def __init__(self) -> None:
        self._base_url = "https://api.mail.tm"

    async def _interact(
        self,
        method: t.Literal["GET", "POST", "DELETE", "PATCH"],
        url: str,
        body: t.Optional[t.Any] = None,
        params: t.Optional[t.Dict[str, str]] = None,
    ) -> t.Optional[bytes]:
        if method not in ["GET", "POST", "DELETE", "PATCH"]:
            raise ValueError("Invalid HTTP method")
        try:
            async with aiohttp.request(method, url, params=params, json=body) as resp:
                result = resp
                if result.status == 200:
                    return await result.read()
                elif result.status == 400:
                    raise MissingArgument(
                        "Something in your payload is missing! Or, the payload isn't there at all."
                    )
                elif result.status == 401:
                    raise AccountTokenInvalid(
                        "Your token isn't correct (Or the headers hasn't a token at all!). Remember, every request (Except POST /accounts and POST /token) should be authenticated with a Bearer token!"
                    )
                elif result.status == 404:
                    raise EntityNotFound(
                        "You're trying to access an account that doesn't exist? Or maybe reading a non-existing message? Go check that!"
                    )
                elif result.status == 405:
                    raise MethodNotAllowed(
                        "Maybe you're trying to GET a /token or POST a /messages. Check the path you're trying to make a request to and check if the method is the correct one."
                    )
                elif result.status == 418:
                    raise RefusedToProcess(
                        "Server is a teapot. And refused to process your request at the moment. Kindly contact the developers for further details."
                    )
                elif result.status == 422:
                    raise EntityNotProcessable(
                        "Some went wrong on your payload. Like, the username of the address while creating the account isn't long enough, or, the account's domain isn't correct. Things like that."
                    )
                elif result.status == 429:
                    raise RatelimitError(
                        "You exceeded the limit of 8 requests per second! Try delaying the request by one second!"
                    )
                else:
                    raise ValueError(f"Unknown Error\nPayload: {await resp.read()}")
        except Exception as e:
            print(f"{str(e)}")

    async def create_account(self, address: str, password: str) -> t.Optional[Account]:
        body = {"address": f"{address}", "password": f"{password}"}
        resp = await self._interact(
            method="POST",
            url=urllib.parse.urljoin(self._base_url, AccountMethods.CREATE_ACCOUNT),
            body=body,
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=Account, strict=False)
        else:
            return None

    async def get_account(self, account_id: str) -> t.Optional[Account]:
        resp = await self._interact(
            method="POST",
            url=urllib.parse.urljoin(
                self._base_url, AccountMethods.GET_ACCOUNT_BY_ID.format(id=account_id)
            ),
            params={"id": f"{account_id}"},
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=Account, strict=False)
        else:
            return None

    async def delete_account(self, account_id: str) -> None:
        await self._interact(
            method="DELETE",
            url=urllib.parse.urljoin(
                self._base_url,
                AccountMethods.DELETE_ACCOUNT_BY_ID.format(id=account_id),
            ),
            params={"id": f"{account_id}"},
        )

    async def get_account_token(
        self, account_address: str, account_password: str
    ) -> t.Optional[Token]:
        body = {"address": f"{account_address}", "password": f"{account_password}"}
        resp = await self._interact(
            method="POST",
            url=urllib.parse.urljoin(self._base_url, AccountMethods.GET_ACCOUNT_TOKEN),
            body=body,
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=Token, strict=False)
        else:
            return None

    async def get_domain(self, domain_id: str) -> t.Optional[Domain]:
        resp = await self._interact(
            method="GET",
            url=urllib.parse.urljoin(
                self._base_url, DomainMethods.GET_DOMAIN_BY_ID.format(id=domain_id)
            ),
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=Domain, strict=False)
        else:
            return None

    async def get_domains(self) -> t.Optional[DomainPageView]:
        resp = await self._interact(
            method="GET",
            url=urllib.parse.urljoin(self._base_url, DomainMethods.GET_ALL_DOMAINS),
        )
        if resp is not None:
            return msgspec.json.decode(resp, type=DomainPageView, strict=False)
        else:
            return None
