import sqlite3
#pieslēgties DB
db = sqlite3.connect('dati-3.db') #(':memory:') ja testē pagaidām

sql = db.cursor() # bez šitā nevar

sql.execute("""CREATE TABLE IF NOT EXISTS darbinieki (
            id INTEGER NOT NULL UNIQUE,
            vards TEXT,
            alga REAL,
            PRIMARY KEY ("id" AUTOINCREMENT)
           )""")

sql.execute("SELECT * FROM darbinieki")
rezultats = sql.fetchall()
print(rezultats)

vards = input("Ievadi vārdu:")
alga = input("Ievadi algu:")

# vaicajums1 = f"INSERT INTO darbinieki VALUES (null, '{vards}', {alga})"
# prepared statement
sql.execute("INSERT INTO darbinieki (vards,alga) VALUES (:vards, :alga)",{'id': 'null', 'vards': vards, 'alga': alga})


# sql.execute(vaicajums1)

sql.execute("SELECT * FROM darbinieki")
rezultats = sql.fetchall()
print(rezultats)


vards = input("Kuru personu?")
sql.execute("SELECT * FROM darbinieki WHERE vards = :kuru", {'kuru': vards})
rezultats = sql.fetchall()
print(rezultats)

#saglabāt izmaiņas
db.commit()

# Nekad neaizmirst aiztaisīt savienojumu
db.close()