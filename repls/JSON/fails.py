import json

def darbibaArFailu():
  with open('valstis.json') as f:
    dati= json.load(f)
    valstis = dati['valstis']
    
  for valsts in valstis:
    del valsts['dial_code']

  with open('jaunas_valstis.json', 'w') as f:
    json.dump(valstis, f, indent=2)

def vaiFailsEksiste():
  import os.path
  print(os.path.isfile('main.txt'))
  print(os.path.isfile('jaunas_valstis.json'))
  print(os.path.isfile('valstis.json'))