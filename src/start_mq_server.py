from movie_quotes.framework.server.server import PieServer
from movie_quotes.main import app
from movie_quotes.framework.server import database
import os

os.remove("movie_quotes.db")

conn , c = database.connect("movie_quotes.db")
c.createTable("moviequotes", ["movie","quote"], c)
c.createEntry("moviequotes", ["movie","quote"], ["tyler", "i dont care"], c)
database.close(conn)

PieServer(app).run()
