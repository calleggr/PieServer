# PyServer
The Python WSGI Webserver for CSSE432 by Tyler Rockwood & Greg Callegari

## Project Summary
The proposal is to implement [PEP 3333](https://www.python.org/dev/peps/pep-3333/) by building a web server, completely in Python. The web server will be built completely to the standard from the [original project](https://www.rose-hulman.edu/class/csse/csse432/201530/Project/WebServer/index.html). In addition to this server, a minimalistic python framework will be implemented on top of the server, similar the frameworks found [here](http://en.wikipedia.org/wiki/Web_Server_Gateway_Interface#WSGI-compatible_applications_and_frameworks). The purpose of this framework will be for the end user to write python web applications on our server, much more simply than FastCGI or other ways that Python is used in web development.

## Project Specification
### Server:

1. GET Requests
1. POST Requests
1. HEAD Requests
1. Error Codes: 200, 301, 400, 404, 500, & 501
1. Request Headers: Host, User-Agent, Connection, Accept, Cookie
1. Response Headers: Date, Server, Content-Length, Connection, Content-Type, Set-Cookie, Location
1. Persistent Connections: Implemented as in the original project
1. Multiple Connections: Each connection will be handled in a separate thread.
1. Implement SSL support

### Framework:
Example usage would be similar to [Flask](http://flask.pocoo.org/) or [WebApp2](https://webapp-improved.appspot.com/tutorials/quickstart.html).
Able to define GET or POST Request Handlers for an arbitrary path
Access Headers, Error Codes and Cookies
Be able to write to the body output using a stringbuffer.

## Proof of Concept:
As proof of concept, we will implement a basic website that uses every aspect of our framework and uses the [Jinja2](http://jinja.pocoo.org/) templating library to output HTML content, and [SQLite](https://docs.python.org/2/library/sqlite3.html#module-sqlite3) for persistent storage.

## Limitations
Only able to use the python modules in the Server implementation:

1. [\__builtin\__](https://docs.python.org/2/library/__builtin__.html#module-__builtin__)
1. [datetime](https://docs.python.org/2/library/string.html#module-string)
1. [string](https://docs.python.org/2/library/string.html#module-string)
1. [Low-level Sockets](https://docs.python.org/2/library/socket.html#module-socket)
1. [SSL](https://docs.python.org/2/library/ssl.html#module-ssl)
1. [Threading or Multiprocessing](https://docs.python.org/2/library/__builtin__.html#module-__builtin__)
