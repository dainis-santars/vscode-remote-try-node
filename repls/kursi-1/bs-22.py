import sqlite3
#pieslēgties DB
db = sqlite3.connect('dati-2.db') #(':memory:') ja testē pagaidām

sql = db.cursor() # bez šitā nevar

sql.execute("""CREATE TABLE IF NOT EXISTS darbinieki (
            id INTEGER NOT NULL UNIQUE,
            vards TEXT,
            alga REAL,
            PRIMARY KEY ("id" AUTOINCREMENT)
           )""")

sql.execute("INSERT INTO darbinieki VALUES (null,'Maris',123.32)")
rezultats = sql.fetchall()
print(rezultats)

sql.execute("SELECT * FROM darbinieki")
rezultats = sql.fetchall()
print(rezultats)

#saglabā datus DB
db.commit()

#aizver konekciju
db.close()