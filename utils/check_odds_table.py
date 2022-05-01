import sqlite3

# https://docs.python.org/3/library/sqlite3.html

conn = sqlite3.connect('db/betting.sqlite')

cur = conn.cursor()

for row in cur.execute('SELECT * from odds'):
    print(row)

conn.close()
