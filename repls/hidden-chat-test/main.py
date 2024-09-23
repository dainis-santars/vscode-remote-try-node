from flask import Flask, render_template
import json
import os
app = Flask('app')

@app.route('/', methods=['GET', 'POST'])
def home():
  return render_template('index.html')

@app.route('/sutit/<zina>')
def sutit(zina):
  # "/sutit/Labrīt visiem!"
  rinda = {"zina": zina}
  with open('dati/chats.json', 'r', encoding="utf-8") as r:
    vecie = r.read()
    rindas = json.loads(vecie)
    rindas.append(rinda)
  
  with open('dati/chats.json', 'w', encoding="utf-8") as f:
    f.write(json.dumps(rindas, indent=2, ensure_ascii=False))

  return "OK"

@app.route('/lasit')
def lasit():
  with open('dati/chats.json', 'r', encoding="utf-8") as f:
    chats = f.read()
  
  return chats

app.run(host='0.0.0.0', port=8080)