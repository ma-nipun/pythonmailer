class SmtpCredentials:
    def __init__(self):
        self.server = "smtp.gmail.com",
        self.sender = "youremailgoeshere.com",
        self.password = "yourapppasword",
        self.port = 465

# Work in Progress
class MassageInfo:
    def __init__(self, subject, massage):
        self.subject = subject
        self.massage = massage
        self.files = []
