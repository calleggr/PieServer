
import os

from framework.server.upload import Upload
from framework import pie_server

PATH = os.path.dirname(__file__)

class TestHandler(pie_server.RequestHandler):

    def head(self):
        pass

    def get(self):
        file = open(os.path.join(PATH, "templates/index.html"))
        self.response.write(file.read())

    def post(self):
        email = self.request.qs_lookup('email')
        name = self.request.qs_lookup('name')
        self.response.write("Name: {0}, Email: {1}".format(name, email))

class FileHandler(pie_server.RequestHandler):

    def get(self):
        file = open(os.path.join(PATH, "templates/uploads.html"))
        self.response.write(file.read())

    def post(self):
        name = self.request.qs_lookup('name')
        file = Upload('', '') or self.request.get_upload('file')
        self.response.write("Name: {0}, Filename: {1}\r\n\r\n".format(name, file.name))
        self.response.write(file.data)

app = pie_server.App( {'/' : TestHandler, '/upload': FileHandler} )
