
import os
import json
from framework.server.upload import Upload
from framework import pie_server
from framework import database

PATH = os.path.dirname(__file__)

class StaticFileHandler(pie_server.RequestHandler):
    def get(self):
        file = open(os.path.join(PATH, self.get_file()))
        self.response.write(file.read())

    def get_file(self):
        return 'public' + self.request.path

class IndexFileHandler(StaticFileHandler):
    def get_file(self):
        return 'public/index.html'

class ZZZZ_API(pie_server.RequestHandler):
    def get(self):
        conn, c = database.connect("movie_quotes.db")
        return_cont = database.readAll("moviequotes",c)
        database.close(conn)
        return_cont = [{'id':v[0], 'movie':v[1], 'quote':v[2]} for v in return_cont]
        self.response.write(json.dumps(return_cont))

    def post(self):
        movie = self.request.params["movie"]
        quote = self.request.params["quote"]
        conn, c = database.connect("movie_quotes.db")
        database.createEntry("moviequotes", ["movie","quote"], [movie, quote], c)
        _id = readAll("moviequotes",c)[-1][0]
        database.close(conn)
        self.response.write(json.dumps({'id':_id}))

    def delete(self):
        _id = self.request.params["id"]
        conn, c = database.connect("movie_quotes.db")
        database.deleteEntry("moviequotes","ID", _id, c)
        database.close(conn)

    def put(self):
        movie = self.request.params["movie"]
        quote = self.request.params["quote"]
        _id = self.request.params["id"]
        conn, c = database.connect("movie_quotes.db")
        database.updateEntry("moviequotes","movie",movie,"ID",_id,c)
        database.updateEntry("moviequotes","quote",quote,"ID",_id,c)
        database.close(conn)

static_files = []
for file in os.walk("public"):
    static_files += [file[0][6:] + '/' + f for f in file[2]]

paths = {'/' : IndexFileHandler}

for file in static_files:
    paths[file] = StaticFileHandler

app = pie_server.App(paths)
