
import os

from framework import pie_server

PATH = os.path.dirname(__file__)

class TestHandler(pie_server.RequestHandler):

    def get(self):
        file = open(os.path.join(PATH, "templates/index.html"))
        self.response.write(file.read())

    def post(self):
        pass

app = pie_server.App( {'/' : TestHandler} )
