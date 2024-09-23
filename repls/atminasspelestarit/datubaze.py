import sqlite3
DB = sqlite3.connect('top.db')
SQL = db.cursor()


def atslegt():
  DB.close()

def taisitTabulu():
  sql.execute("""CREATE TABLE rezultati (
              id INTEGER NOT NULL UNIQUE,
              vards TEXT,
              vecums INTEGER
              laiks INTEGER
              klikski INTEGER
              datums TEXT
              piezimes TEXT
              skola TEXT
              PRIMARY KEY("id" AUTOINCREMENT)
             )""")

taisitTabulu()