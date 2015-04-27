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

print '===BEGIN HEAD TEST 1 ==='
print 'Testing HTTP v1.0 HEAD request'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
request = """HEAD /index.html HTTP/1.0\r\n"""
s.sendall(request)
data = s.recv(1024)
response_lines = data.split('\r\n')
expected = 'HTTP/1.1 200 OK'
print 'Expecting line 1 of response to be: ', expected
print 'Got: ', response_lines[0]

if expected == response_lines[0]:
    print 'PASSED TEST 1'
else:
    print 'FAILED TEST 1'
s.close()

print '===BEGIN HEAD TEST 2 ==='
print 'Testing HTTP v1.1 HEAD request'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
request = """HEAD / HTTP/1.1\r\nHost: 127.0.0.1\r\n"""
s.sendall(request)
data = s.recv(1024)
response_lines = data.split('\r\n')
expected = 'HTTP/1.1 200 OK'
print 'Expecting line 1 of response to be: ', expected
print 'Got: ', response_lines[0]
if expected == response_lines[0]:
    print 'PASSED TEST 2'
else:
    print 'FAILED TEST 2'

print '===BEGIN HEAD TEST 3 ==='
print 'Testing HTTP v1.1 HEAD request with headers'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
request = """HEAD / HTTP/1.1\r\nHost: 127.0.0.1\r\nAccept: text/plain\r\nAccept-Language: en-us\r\n"""
s.sendall(request)
data = s.recv(1024)
response_lines = data.split('\r\n')
expected_lines = ['HTTP/1.1 200 OK',
                  'Date: (\w\w\w), (\d\d) (\w\w\w) (\d\d\d\d) (\d\d):(\d\d):(\d\d) ([A-Z]+)' ,
                  'Server: (\w+)',
                  'Content-Length: (\d+)']
print 'Expecting lines of response to be: ', expected_lines
print 'Got: ', response_lines
test_passed = True
line_in_resp = lambda expected_line: ormap(lambda line: re.match(expected_line, line), response_lines)
test_passed = andmap(line_in_resp, expected_lines)
if test_passed:
    print 'PASSED TEST 3'
else:
    print 'FAILED TEST 3'
