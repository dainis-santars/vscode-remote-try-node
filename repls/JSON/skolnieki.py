import json

def skolnieksNoJSON():
  json_obj =  '{ "vards": "Davis", "gadi": 16, "klase":"11" }'
  python_obj = json.loads(json_obj)
  print("\nJSON data:")
  print(python_obj)
  print("\nvards: ",python_obj["vards"])
  print("klase: ",python_obj["klase"])
  print("gadi: ",python_obj["gadi"]) 

def skolnieksUzJSON():
  # a Python object (dict):
  python_obj = {
  "vards": "David",
  "klase":"11",
  "gadi": 16  
  }
  print(type(python_obj))
  # convert into JSON:
  j_data = json.dumps(python_obj)

  # result is a JSON string:
  print(j_data)

def kartot():
  j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
  print("Orģināli:")
  print(j_str)
  print("\nJSON dati:")
  print(json.dumps(j_str, sort_keys=True, indent=4))