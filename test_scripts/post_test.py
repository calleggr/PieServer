import re
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 8080              # The same port as used by the server

### TEST HELPER METHODS ###
# Note I'm not concerned about efficency, just clarity
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
request = """POST / HTTP/1.1\r\nHost: 127.0.0.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 46\r\n\r\nname=Tyler+Rockwood&email=rockwotj%40gmail.com\r\n\r\n"""
s.sendall(request)
data = s.recv(4096)
response_lines = data.split('\r\n')
expected_lines = ['HTTP/1.1 200 OK', 'Content-Length: (\d+)', "Name: Tyler Rockwood, Email: rockwotj@gmail.com"]
print 'Expecting lines of response to be at least: ', expected_lines
print 'Got: ', response_lines
test_passed = True
line_in_resp = lambda expected_line: ormap(lambda line: re.match(expected_line, line), response_lines)
test_passed = andmap(line_in_resp, expected_lines)
if test_passed:
    print 'PASSED TEST 1'
else:
    print 'FAILED TEST 1'
