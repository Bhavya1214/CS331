import smtplib
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.port = 587
        self.email_user = "theendlessblue09@gmail.com"
        self.email_pass = "vbdx uwln sbzs ohwi"

    def send(self, email, response):
        msg = MIMEText(response)
        msg["From"] = self.email_user
        msg["To"] = email.sender
        msg["Subject"] = "Re: " + email.subject

        server = smtplib.SMTP(self.smtp_server, self.port)
        server.starttls()
        server.login(self.email_user, self.email_pass)
        server.send_message(msg)
        server.quit()

        print("[EmailSender] Reply sent successfully")
        email.status = "RESPONDED"
