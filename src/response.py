from datetime import datetime

class Response():
    RESPONSE_MESSAGES = {200: 'OK', 404: "Not Found", 100: "Continue", 301: "Moved Permanently", 400: "Bad Request", 405: "Method Not Allowed", 500: "Internal Server Error"}

    def __init__(self):
        self.set_status()
        self.headers = {}
        now = datetime.utcnow()
        fmt = "%a, %d %b %Y %X UTC"
        self.headers["Date"] = now.strftime(fmt)
        #TODO get creative, perhaps consult a liberal arts major
        self.headers["Server"] = 'PyServer'
        self.headers["Content-Length"] = 0

    def set_status(self, status_code=200):
        self.status_code = status_code
        self.status_message = Response.RESPONSE_MESSAGES[status_code]

    def __str__(self):
        response = 'HTTP/1.1 ' + str(self.status_code) + ' ' + self.status_message + '\r\n'
        for (name, value) in self.headers.items():
            response += name + ': ' + str(value) + '\r\n'
        return response
