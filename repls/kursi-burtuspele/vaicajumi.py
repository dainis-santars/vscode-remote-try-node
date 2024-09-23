import sqlite3
import json

JSON = 'dati/tests.json'

db = sqlite3.connect('rezultati.db')
sql = db.cursor()

sql.execute("SELECT * FROM rezultati ORDER BY punkti DESC LIMIT 10")
rezultats = sql.fetchall()
# print(rezultats)

tops = []
for rez in rezultats:
  tops.append({
    "id":rez[0],
    "vards":rez[1],
    "punkti":rez[2],
    "laiks":rez[3]
  })

  with open('dati/out.json', 'w', encoding="utf-8") as f:
    f.write(json.dumps(tops, indent=2, ensure_ascii=False))


db.commit()
# Nekad neaizmirst aiztaisīt savienojumu
db.close()

