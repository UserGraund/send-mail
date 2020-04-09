from __future__ import unicode_literals

SMTP_HOST = 'smtp.mailtrap.io'


class Message(object):
    """
    Class which are generating message
    """
    def __init__(self, sender=None, receiver=None, msg=None):
        # type: (str, str, str) -> None
        """
        Specify the senders and receivers email addresses.
        """
        self.sender = sender if sender \
            else "Private Person <from@{0}>".format(SMTP_HOST)
        self.receiver = receiver if receiver \
            else "A Test User <to@{0}>".format(SMTP_HOST)
        self.message = msg

    @property
    def message(self):
        """Get message property."""
        return self._message

    @message.setter
    def message(self, msg=None):
        # type: (str) -> None
        """Set message property."""
        if not msg:
            self._message = """\
            Subject: Hi Mailtrap
            To: {0}
            From: {1}
            This is a test e-mail message.
            """.format(self.receiver, self.sender)
        else:
            self._message = msg
