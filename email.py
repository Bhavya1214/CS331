class Email:
    def __init__(self, sender, receiver, subject, content):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.content = content
        self.category = None
        self.priority = None
        self.status = "RECEIVED"
