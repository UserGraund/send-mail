from __future__ import unicode_literals

import smtplib
import sys

from socket import gaierror

from message import SMTP_HOST, Message

if sys.version_info[0] == 2:
    class ConnectionError(OSError):
        pass

    class ConnectionRefusedError(ConnectionError):
        pass


DEFAULT_LOGIN = 'login'
DEFAULT_PASSWORD = 'password'


class SendEmail:
    """Service to run emails."""
    port = 2525
    smtp_server = SMTP_HOST

    def __init__(self, login=None,  password=None):
        # type: (str, str) -> None

        if login and password:
            self.auth = (login, password)
        else:
            self.auth = (DEFAULT_LOGIN, DEFAULT_PASSWORD)

    def run(self, message_instance):
        # type: (Message) -> None
        smtp_instance = smtplib.SMTP()
        try:
            smtp_instance.connect(host=self.smtp_server, port=self.port)
            smtp_instance.login(*self.auth)
            smtp_instance.sendmail(
                from_addr=message_instance.sender,
                to_addrs=message_instance.receiver,
                msg=message_instance.message
            )
        except (gaierror, ConnectionRefusedError):
            print('Failed to connect to the server. Bad connection settings?')
        except (smtplib.SMTPServerDisconnected,
                smtplib.SMTPAuthenticationError):
            print('Failed to connect to the server. Wrong user/password?')
        except smtplib.SMTPException as exc:
            print('SMTP error occurred: {0}'.format(str(exc)))
        else:
            print('Sent')
        finally:
            smtp_instance.close()
