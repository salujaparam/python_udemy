import sqlite3
import csv

conn = sqlite3.connect('movies.sqlite')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Movies (movie_name TEXT, release_date TEXT, public_rating INTEGER, critic_rating INTEGER, genre TEXT, film_industry TEXT, actors TEXT, director TEXT, producer TEXT)")

with open('movies.csv') as csvfile:
    movies = list(csv.DictReader(csvfile))
columns = list()
for column in movies[0]:
    columns.append(column)
print(columns)
# for movie in movies:
#     for key, value in movie.items():
#         print(key, value)
