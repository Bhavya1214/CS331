import smtplib
from email.mime.text import MIMEText

EMAIL = "theendlessblue09@gmail.com"
PASSWORD = "vbdx uwln sbzs ohwi"

def send_email(to_email, subject, body):

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)

        server.sendmail(EMAIL, to_email, msg.as_string())
        server.quit()

        print("Email sent to", to_email)

    except Exception as e:
        print("Error:", e)