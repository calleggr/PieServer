import re
import socket

HOST = 'www.example.com'    # The remote host
PORT = 80              # The same port as used by the server

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
print '===BEGIN GET TEST 1 ==='
print 'Testing HTTP v1.0 GET request'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
request = """GET /index.html HTTP/1.0\r\n\r\n"""
s.sendall(request)
data = s.recv(4096)
response_lines = data.split('\r\n')
expected = 'HTTP/1.0 200 OK'
print 'Expecting line 1 of response to be: ', expected
print 'Got: ', data#response_lines[0]

if expected == response_lines[0]:
    print 'PASSED TEST 1'
else:
    print 'FAILED TEST 1'
s.close()