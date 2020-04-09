from send_mail import SendEmail
from message import Message

if __name__ == "__main__":
    SendEmail("11113d506b95d4", "079598811116b1").run(
        message_instance=Message()
    )
