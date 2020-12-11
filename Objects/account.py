class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def __str__(self):
        return "username is '%s', password is '%s" % (self.username, self.password)
