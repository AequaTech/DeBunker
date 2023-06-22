import sqlite3
con = sqlite3.connect("dubunkerAPI.db")
cur = con.cursor()
cur.execute("CREATE TABLE  IF NOT EXISTS urls(hash_id CHAR PRIMARY KEY, url CHAR UNIQUE, title TEXT, content TEXT, date DATE KEY)")
con.close()