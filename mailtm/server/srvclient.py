import typing as t

from .srv import MailServer
from ..abc.modals import Message, Domain


class Server(MailServer):
    async def _check_for_new_messages(self) -> t.Optional[Message]:
        msg_view = await self.mail_client.get_messages()
        if msg_view and msg_view.messages:
            if not self._last_msg or self._last_msg[0].id != msg_view.messages[0].id:
                if self._last_msg:
                    self._last_msg[0] = msg_view.messages[0]
                else:
                    self._last_msg.append(msg_view.messages[0])
                return msg_view.messages[0]
        return None

    async def _check_for_domain_change(self) -> t.Optional[Domain]:
        domain_view = await self.mail_client.get_domains()
        if domain_view and domain_view.domains:
            if (
                not self._last_domain
                or self._last_domain[0].domain_name
                != domain_view.domains[0].domain_name
            ):
                if self._last_domain:
                    self._last_domain[0] = domain_view.domains[0]
                else:
                    self._last_domain.append(domain_view.domains[0])
                return domain_view.domains[0]
        return None
