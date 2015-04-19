from datetime import datetime
import os

class Response():
    RESPONSE_MESSAGES = {200: 'OK', 404: "Not Found", 100: "Continue", 301: "Moved Permanently", 400: "Bad Request", 405: "Method Not Allowed", 500: "Internal Server Error"}

    def __init__(self):
        self.set_status()
        self.headers = {}
        now = datetime.utcnow()
        fmt = "%a, %d %b %Y %X UTC"
        self.headers["Date"] = now.strftime(fmt)
        self.headers["Server"] = 'PieServer'
        self.headers["Content-Length"] = 0
        self.body = ""

    def set_status(self, status_code=200):
        self.status_code = status_code
        self.status_message = Response.RESPONSE_MESSAGES[status_code]

    def write(self, data):
        self.body += data
        self.headers["Content-Length"] += len(data)

    def __str__(self):
        response = 'HTTP/1.1 ' + str(self.status_code) + ' ' + self.status_message + '\r\n'
        for (name, value) in self.headers.items():
            response += name + ': ' + str(value) + '\r\n'
        response += '\r\n'
        response += self.body
        return response

def not_found_response():
    response = Response()
    response.set_status(404)
    file = open(os.path.join(os.path.dirname(__file__), "error_pages/404.html"))
    response.write(file.read())
    return response
