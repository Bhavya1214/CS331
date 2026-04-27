import imaplib
import email
import re

def fetch_emails():

    # connect to gmail server
    mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)

    # login to email
    mail.login("theendlessblue09@gmail.com", "vbdx uwln sbzs ohwi")

    mail.select("inbox")

    # ✅ fetch only unseen emails
    status, messages = mail.search(None, "UNSEEN")

    email_ids = messages[0].split()

    emails = []

    for eid in email_ids:

        status, msg_data = mail.fetch(eid, "(RFC822)")

        raw_email = msg_data[0][1]

        msg = email.message_from_bytes(raw_email)

        from_email = msg["from"]
        subject = msg["subject"]

        # extract clean email
        match = re.findall(r'<(.+?)>', from_email)
        if match:
            from_email = match[0]

        emails.append({
            "from": from_email,
            "subject": subject
        })

        # ✅ mark as read
        mail.store(eid, '+FLAGS', '\\Seen')

    mail.logout()

    return emails