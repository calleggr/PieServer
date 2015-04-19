
from ..framework import pie_server


class TestHandler(pie_server.RequestHandler):

    def get(self):
        self.response.write('Hello World!')


app = pie_server.App( {'/' : TestHandler} )
