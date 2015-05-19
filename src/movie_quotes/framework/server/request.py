from errors import ServerError
import urllib
import json

class Request():

    ALLOWED_METHODS = ['HEAD', 'GET', 'POST', 'PUT', 'DELETE']

    def __init__(self, request_text):
        request_text = request_text.split('\r\n\r\n', 1)
        if len(request_text) > 1:
            self.body = request_text[1].strip()
        else:
            self.body = ""
        header_lines = request_text[0].split('\r\n')
        command = header_lines[0].split(' ')
        if len(command) != 3:
            raise ServerError('Invalid Request, malformed command', 400)
        self.method = command[0]
        if self.method not in Request.ALLOWED_METHODS:
            raise ServerError('Not Supported Request', 405)
        command[1] = command[1].split('?', 1)
        self.path = command[1][0]
        self.params = []
        if len(command[1]) > 1:
            self._qs = command[1][1]
            self._parse_parameters(self.params, self._qs)
        if not self.path.startswith('/'):
            self.path = self.path(self.path.split('/', 1)[-1])
        self.version = command[2]
        self.headers = {}
        for header_line in header_lines[1:]:
            if header_line == "":
                continue
            header = header_line.split(': ', 1)
            name = header[0]
            value = header[1]
            self.headers[name] = value
        if self.version.endswith('1.1') and not self.headers.get('Host'):
            raise ServerError('Invalid Request, no host in header', 400)
        if self.method == 'POST' or self.method == 'PUT':
            if 'application/json' in self.headers.get('Content-Type', ""):
                self.params += json.loads(self.body).items()
            elif 'application/x-www-form-urlencoded' in self.headers.get('Content-Type', ""):
                self._parse_parameters(self.params, self.body)

    def _parse_parameters(self, list, params):
        for param in params.split('&'):
            param = urllib.unquote_plus(param).split('=', 1)
            list.append((param[0],param[1]))

    def qs_lookup(self, key, default=None):
        for kee, value in self.params:
            if key == kee:
                return value
        return default


if __name__ == '__main__':
    pass
