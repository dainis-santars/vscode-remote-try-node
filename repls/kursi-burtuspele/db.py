import sqlite3
import json

JSON = 'dati/tests.json'

DB = sqlite3.connect('rezultati.db')
SQL = DB.cursor()

SQL.execute("""CREATE TABLE IF NOT EXISTS rezultati ( 
              id INTEGER NOT NULL UNIQUE,
              vards TEXT,
              punkti INTEGER,
              laiks TEXT,
              PRIMARY KEY("id" AUTOINCREMENT)
           )""")

with open(JSON, 'r', encoding="UTF-8") as f:
  dati = f.read()
  datiJson = json.loads(dati)
  for dati in datiJson:
    print(datiJson)
  SQL.execute("INSERT INTO rezultati (vards, punkti, laiks) VALUES (:vards, :punkti, :laiks)", {'vards': dati['vards'], 'punkti': dati['punkti'],'laiks': dati['laiks']})



DB.commit()

SQL.execute("SELECT * FROM rezultati")

print(SQL.fetchall())