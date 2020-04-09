import unittest

from message import Message


class MessageTestCase(unittest.TestCase):
    def setUp(self):
        super(MessageTestCase, self).setUp()
        self.sender = 'test'
        self.receiver = 'test'

    def test_property_message_setter_initialized_with_empty_message(self):
        """
        Case: message instance is initialized
        Expected: message instance set default value
        """
        msg_instance = Message(receiver=self.receiver, sender=self.sender)
        self.assertEqual(
            msg_instance.message,
            """\
            Subject: Hi Mailtrap
            To: {0}
            From: {1}
            This is a test e-mail message.
            """.format(self.receiver, self.sender)
        )

    def test_property_message_setter_initialized_with_message_value(self):
        """
        Case: message instance is initialized with
        Expected: message instance set default value
        """
        msg_instance = Message(
            receiver=self.receiver,
            sender=self.sender,
            msg='test'
        )
        self.assertEqual(
            msg_instance.message,
            'test'
        )
