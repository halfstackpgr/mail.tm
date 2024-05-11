from mailtm.server.events import NewMessage

from mailtm.core.methods import ServerAuth

from mailtm.server.srv import MailServerBase

from mailtm.impls.pullers import get

get_ac = get().get_account_token(account_address="jsfdonelass@fthcapital.com", account_password=r"lovejihadontop")

cs = MailServerBase(
    server_auth=ServerAuth(
        account_id=get_ac.id, #type: ignore
        account_token=get_ac.token), #type: ignore
    pooling_rate=1,
    banner=True,
    enable_logging=True
)


@cs.on_new_message
async def event(event: NewMessage):
    await event.delete_message()


cs.run()