import sqlite3
conn=sqlite3.connect("BD1.db")
#conn.execute ("CREATE TABLE personas (id INTEGER PRIMARY KEY,nombre TEXT,fecha date);")
#conn.execute ("insert into personas (nombre) values ('PAblo');")
#conn.execute("drop table personas;")
conn.execute("select * FROM personas;")