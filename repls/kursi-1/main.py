import sqlite3
#pieslēgties DB
db = sqlite3.connect('dati-3.db') #(':memory:') ja testē pagaidām
sql = db.cursor() # bez šitā nevar

vards = input("Kuru personu?")
sql.execute("SELECT * FROM darbinieki WHERE vards = :kuru", {'kuru': vards})

# rezultats = sql.fetchmany(2) ja parādīt dažus
rezultats = sql.fetchall()

for darbinieks in rezultats:
  print('ID:',darbinieks[0])
  print('Vārds:',darbinieks[1])
  print('Alga:',darbinieks[2])
  


# Nekad neaizmirst aiztaisīt savienojumu
db.close()