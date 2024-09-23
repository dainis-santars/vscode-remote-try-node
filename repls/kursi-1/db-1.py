import sqlite3
#pieslēgties DB
db = sqlite3.connect(':memory:') #memory strāda pa tiešo ar RAM, neko neglabā, der fiksai testēšanai

sql = db.cursor() # bez šitā nevar

sql.execute("""CREATE TABLE darbinieki (
            id INTEGER NOT NULL UNIQUE,
            vards TEXT,
            alga REAL,
            PRIMARY KEY ("id" AUTOINCREMENT)
           )""")

sql.execute("INSERT INTO darbinieki (vards,alga) VALUES ('Maris',123.32)")
rezultats = sql.fetchall()
print(rezultats)

sql.execute("SELECT * FROM darbinieki")
rezultats = sql.fetchall()
print(rezultats)

#aizver konekciju
db.close()