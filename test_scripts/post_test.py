import re
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 8080              # The same port as used by the server

### TEST HELPER METHODS ###

def ormap(func, seq):
    result = False
    booleans = map(func, seq)
    for b in booleans:
        result = bool(b) or result
    return result

def andmap(func, seq):
    result = True
    booleans = map(func, seq)
    for b in booleans:
        result = bool(b) and result
    return result

### START TESTS ###
### The POST handler should echo back a parsed  ###
print '===BEGIN GET TEST 1 ==='
print 'Testing HTTP v1.0 GET request'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
request = """GET / HTTP/1.0\r\n"""
s.sendall(request)
data = s.recv(4096)
response_lines = data.split('\r\n')
expected = 'HTTP/1.1 200 OK'
print 'Expecting line 1 of response to be: ', expected
print 'Got: ', response_lines[0]

if expected == response_lines[0]:
    print 'PASSED TEST 1'
else:
    print 'FAILED TEST 1'
s.close()
