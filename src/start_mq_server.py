from movie_quotes.framework.server.server import PieServer
from movie_quotes.main import app
from movie_quotes.framework import database
import os

if os.path.isfile("movie_quotes.db"):
    os.remove("movie_quotes.db")

conn , c = database.connect("movie_quotes.db")
database.createTable("moviequotes", ["movie","quote"], c)
database.createEntry("moviequotes", ["movie","quote"], ["tyler", "i dont care"], c)
database.close(conn)

PieServer(app).run()
