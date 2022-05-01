import sqlite3

con = sqlite3.connect('db/betting.sqlite')

cur = con.cursor()

cur.execute('''CREATE TABLE odds
               (id text,
               sport_key text,
               sport_nice text,
               team_a text,
               team_b text,
               home_team text,
               commence_time text)''')

con.commit()

con.close()
