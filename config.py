class SmtpCredentials:
    def __init__(self, server, sender, password, port):
        self.server = server
        self.sender = sender
        self.password = password
        self.port = port


class MassageInfo:
    def __init__(self, subject, massage):
        self.subject = subject
        self.massage = massage
        self.files = []
