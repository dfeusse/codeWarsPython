'''
Create an SQLite3 database /tmp/movies.db

Your database should have a table named MOVIES that contains the following data:

Name	Year	Rating
Rise of the Planet of the Apes	2011	77
Dawn of the Planet of the Apes	2014	91
Alien	1979	97
Aliens	1986	98
Mad Max	1979	95
Mad Max 2: The Road Warrior	1981	100
'''
import sqlite3

conn = sqlite3.connect('tmp/movies.db')

cursor = conn.cursor()

cursor.execute(""" CREATE TABLE movies (
	Name TEXT, Year INT, Rating INT)
	""")

#cursor.execute("INSERT INTO movies VALUES('Name', Year, Rating)")

movies = [
	('Rise of the Planet of the Apes', 2011, 77),
	('Dawn of the Planet of the Apes', 2014, 91),
	('Alien', 1979, 97),
	('Aliens', 1986, 98),
	('Mad Max',	1979, 95),
	('Mad Max 2: The Road Warrior', 1981, 100)
]

cursor.executemany('INSERT INTO movies VALUES(?,?,?)', movies)

conn.commit()
conn.close()

'''
import sqlite3
from contextlib import closing

with sqlite3.connect('/tmp/movies.db') as db:
  with closing(db.cursor()) as cursor:
    cursor.execute('''
        CREATE TABLE MOVIES(id INTEGER PRIMARY KEY, 
                            Name TEXT unique,
                            Year INTEGER, 
                            Rating INTEGER)
    ''')
    
    movies = [("Rise of the Planet of the Apes", 2011, 77),
              ("Dawn of the Planet of the Apes", 2014, 91),
              ("Alien", 1979, 97),
              ("Aliens", 1986, 98),
              ("Mad Max", 1979, 95),
              ("Mad Max 2: The Road Warrior", 1981, 100)]
    
    cursor.executemany("INSERT INTO MOVIES(Name, Year, Rating) VALUES(?,?,?)", movies)
    db.commit()


import sqlite3
movies = [
  { 'Name' : 'Rise of the Planet of the Apes', 'Year' : 2011, 'Rating' : 77 },
  { 'Name' : 'Dawn of the Planet of the Apes', 'Year' : 2014, 'Rating' : 91 },
  { 'Name' : 'Alien',                          'Year' : 1979, 'Rating' : 97 },
  { 'Name' : 'Aliens',                         'Year' : 1986, 'Rating' : 98 },
  { 'Name' : 'Mad Max',                        'Year' : 1979, 'Rating' : 95 },
  { 'Name' : 'Mad Max 2: The Road Warrior',    'Year' : 1981, 'Rating' : 100 }
]
# Create a database /tmp/movies.db using SQLite3
db = sqlite3.connect('/tmp/movies.db')
cursor = db.cursor()

# Create a table in it called "MOVIES"
cursor.execute('create table if not exists MOVIES (Name, Year, Rating)')

# Insert data
cursor.executemany('insert into MOVIES values (:Name, :Year, :Rating)', movies)

db.commit()
db.close()
'''