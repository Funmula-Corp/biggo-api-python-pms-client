class BigGoError(Exception):
    def __init__(self, message: str, code=None):
        super().__init__(message)
        self.code = code

class BigGoAuthError(Exception):
    def __init__(self, message: str, code=None):
        message = message.replace('( app_id )', '( clientID )')
        message = message.replace('( app_key )', '( clientSecret )')
        super().__init__(message)
        self.code = code
