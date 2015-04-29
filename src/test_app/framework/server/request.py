from errors import ServerError

class Request():

    ALLOWED_METHODS = ['HEAD', 'GET', 'POST']

    def __init__(self, request_text):
        request_lines = request_text.split('\r\n')
        command = request_lines[0].split(' ')
        if len(command) != 3:
            raise ServerError('Invalid Request, malformed command', 400)
        self.method = command[0]
        if self.method not in Request.ALLOWED_METHODS:
            raise ServerError('Not Supported Request', 405)
        self.path = command[1]
        # TODO: Parse query string...
        if not self.path.startswith('/'):
            self.path = self.path(self.path.split('/', 1)[-1])
        self.version = command[2]
        self.headers = {}
        for header_line in request_lines[1:]:
            if header_line == "":
                continue
            header = header_line.split(': ', 1)
            name = header[0]
            value = header[1]
            self.headers[name] = value
        if self.version.endswith('1.1') and not self.headers.get('Host'):
            raise ServerError('Invalid Request, no host in header', 400)
        if self.method == 'POST':
            # TODO: Parse POST Body
            pass

if __name__ == '__main__':
    pass
