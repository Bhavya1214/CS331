import imaplib
import email
from email.header import decode_header
from email import policy
from email.parser import BytesParser
from email import message_from_bytes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from email import Email   # your Email class

class EmailService:
    def __init__(self):
        self.imap_server = "imap.gmail.com"
        self.email_user = "theendlessblue09@gmail.com"
        self.email_pass = "vbdx uwln sbzs ohwi"

    def receive_email(self):
        mail = imaplib.IMAP4_SSL(self.imap_server)
        mail.login(self.email_user, self.email_pass)
        mail.select("inbox")

        status, messages = mail.search(None, "UNSEEN")
        email_ids = messages[0].split()

        if not email_ids:
            print("[EmailService] No new emails")
            return None

        latest_email_id = email_ids[-1]
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = msg_data[0][1]

        msg = message_from_bytes(raw_email)

        sender = msg["From"]
        subject = msg["Subject"]

        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
        else:
            body = msg.get_payload(decode=True).decode()

        mail.logout()

        print("[EmailService] Email received from:", sender)

        return Email(
            sender=sender,
            receiver=self.email_user,
            subject=subject,
            content=body
        )
