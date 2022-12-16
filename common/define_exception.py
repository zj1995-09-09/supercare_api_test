class DException(Exception):

    def __init__(self, msg=None):
        super().__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg
