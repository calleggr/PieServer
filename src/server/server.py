import socket
from response import Response, not_found_response
from request import Request
from errors import ServerError
from ..app.main import app

HOST = ''
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)
print "Listing on port: " + str(PORT)
while True:
    conn, addr = s.accept()
    print "Accepted connection from: " + str(addr)
    data = conn.recv(4096)
    response = Response()
    try:
        request = Request(data)
    except ServerError, e:
        print "Request Error: ", e.message
        response.set_status(status_code=e.code)
        conn.sendall(str(response))
        conn.close()
        continue
    if request.path in app.paths:
        handler = app.paths[request.path](request, response)
        try:
            handler.handle()
        except ServerError, e:
            print "Request Error: ", e.message
            response.set_status(status_code=e.code)
            conn.sendall(str(response))
            conn.close()
            continue
    else:
        response = not_found_response()
    conn.sendall(str(response))
    conn.close()
