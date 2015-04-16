class ServerError(Exception):
    def __init__(self, message, error_code):
        super(Exception, self).__init__(message)
        self.code = error_code
