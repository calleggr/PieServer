from server.errors import ServerError

class RequestHandler():

    def __init__(self, request, response):
        self.response = response
        self.request = request

    def handle(self):
        method = self.request.method.lower()
        if not hasattr(self, method):
            raise ServerError("No Method: "  + method + " for path: " + self.request.path, 405)
        method_func = getattr(self, method)
        method_func()

class App():

    def __init__(self, paths={}):
        self.paths = paths
