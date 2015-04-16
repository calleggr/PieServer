import socket
from response import Response
from request import Request
from errors import ServerError

HOST = ''
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print "Listing on port: " + str(PORT)
while True:
    conn, addr = s.accept()
    data = conn.recv(4096)
    response = Response()
    try:
        request = Request(data)
    except ServerError, e:
        print "Request Error: ", e.message
        response.set_status(status_code=e.code)
    conn.sendall(str(response))
    conn.close()
