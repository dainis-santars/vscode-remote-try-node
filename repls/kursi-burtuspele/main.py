from flask import Flask, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime
import requests
import db
import vaicajumi

app = Flask('app')
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello_world():
  return 'Burtu spēle'

@app.route('/lasit')
def lasit():
  with open('dati/tests.json', 'r', encoding="utf-8") as f:
    chats = f.read()
  
  return chats

@app.route('/tops')
def tops():
  with open('dati/out.json', 'r', encoding="utf-8") as f:
    tops = f.read()  
  return tops


@app.route('/sutit/<vards>/<punkti>')
def sutit(vards, punkti):
  tagad = datetime.now()
  laiks = tagad.strftime('%d.%m.%Y, %H.%M.%S')
  # "/sutit/Anna/Labrīt visiem!"
  rinda = {
      "vards": vards,
      "punkti": punkti,
      "laiks": laiks
  }
  with open('dati/tests.json', 'r', encoding="utf-8") as r:
    vecie = r.read()
    rindas = json.loads(vecie)
  rindas.append(rinda)
  
  with open('dati/tests.json', 'w', encoding="utf-8") as f:
    f.write(json.dumps(rindas, indent=2, ensure_ascii=False))
    
  return "OK"

app.run(host='0.0.0.0', port=8080)