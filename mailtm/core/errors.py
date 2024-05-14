class MissingArgument(Exception):
    """
    Bad request 400

    Something in your payload is missing! Or, the payload isn't there at all.
    """

    ...


class AccountTokenInvalid(Exception):
    """
    Unauthorized 401

    Your token isn't correct (Or the headers hasn't a token at all!). Remember, every request (Except POST /accounts and POST /token) should be authenticated with a Bearer token!
    """

    ...


class EntityNotFound(Exception):
    """
    Not found 404
    
    You're trying to access an account that doesn't exist? Or maybe reading a non-existing message? Go check that!
    """

    ...


class MethodNotAllowed(Exception):
    """
    Method not allowed 405

    Maybe you're trying to GET a /token or POST a /messages. Check the path you're trying to make a request to and check if the method is the correct one.
    """

    ...


class RefusedToProcess(Exception):
    """
    I'm a teapot 418

    Who knows? Maybe the server becomes a teapot!
    """

    ...


class EntityNotProcessable(Exception):
    """
    Unprocessable entity 422

    Something went wrong on your payload. Like, the username of the address while creating the account isn't long enough, or, the account's domain isn't correct. Things like that.
    """

    ...


class RatelimitError(Exception):
    """
    Too many requests 429
    
    You exceeded the limit of 8 requests per second! Try delaying the request by one second!
    """

    ...
