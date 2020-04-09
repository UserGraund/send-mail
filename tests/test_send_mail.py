from __future__ import unicode_literals

import smtplib
import unittest

from send_mail import SendEmail
from message import Message

try:
    from unittest import mock
except ImportError:
    import mock


class SendMailRunTestCase(unittest.TestCase):
    def setUp(self):
        super(SendMailRunTestCase, self).setUp()
        self.login = 'test'
        self.password = 'test'
        self.message_instance = Message()

    @mock.patch('smtplib.SMTP')
    def test_run_success(self, smtp_mock):
        """
        Case: service is called to send message
        Expected: service sent message success
        """
        service = SendEmail(self.login, self.password)
        service.run(message_instance=self.message_instance)
        smtp_mock.assert_has_calls([
            mock.call().connect(
                host=SendEmail.smtp_server,
                port=SendEmail.port
            ),
            mock.call().login(*(self.login, self.password)),
            mock.call().sendmail(
                from_addr=self.message_instance.sender,
                to_addrs=self.message_instance.receiver,
                msg=self.message_instance.message
            ),
            mock.call().close()
        ])

    @mock.patch('smtplib.SMTP.connect', side_effect=smtplib.SMTPServerDisconnected)
    @mock.patch('smtplib.SMTP.close')
    @mock.patch('sys.stdout')
    def test_run_failed(self, print_mock, smtp_close_mock, smtp_connect_mock):
        """
        Case: service is called to send message
        Expected: service sent message failed,  wrong password or user
        """
        service = SendEmail(self.login, self.password)
        service.run(message_instance=self.message_instance)

        self.assertEqual(smtp_close_mock.call_count, 1)
        smtp_connect_mock.assert_called_once_with(
            host=SendEmail.smtp_server, port=SendEmail.port
        )
        print_mock.assert_has_calls([
            mock.call.write('Failed to connect to the server. Wrong user/password?'),
            mock.call.write('\n')
        ])
