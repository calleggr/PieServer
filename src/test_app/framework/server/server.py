import socket
import threading
from response import Response, not_found_response
from request import Request
from errors import ServerError

class PieServer():

    def __init__(self, app, port=8080):
        self.app = app
        self.port = port

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', self.port))
        s.listen(1)
        print "Listing on port: " + str(self.port)
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_conn, args=(conn, addr, self.app))
            thread.start()

def handle_conn(conn, addr, app):
    print "Accepted connection from: " + str(addr)
    while True:
        try:
            data = conn.recv(2**20)
        except Exception, _:
            print 'Closing connection at: ', addr
            conn.close()
            return
        response = Response()
        try:
            request = Request(data)
        except ServerError, e:
            print "Request Error: ", e.message, '\n', data
            response.set_status(status_code=e.code)
            conn.sendall(str(response))
            conn.close()
            return
        if request.path in app.paths:
            handler = app.paths[request.path](request, response)
            try:
                handler.handle()
            except ServerError, e:
                print "Request Error: ", e.message, '\n', data
                response.set_status(status_code=e.code)
                conn.sendall(str(response))
                conn.close()
                return
        else:
            response = not_found_response()
        conn.sendall(str(response))
        if request.headers.get('Connection') == 'keep-alive':
            conn.settimeout(15)
        else:
            conn.close()
