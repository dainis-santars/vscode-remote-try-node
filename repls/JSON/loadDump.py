import json

def loadJSON():
  stringObjekts =  '{ "vards": "Davis", "gadi": 16, "klase":"11"}'
  y = json.loads(stringObjekts)
  print(y["gadi"])

def dumpJSON():
  jsonObjekts = {'lalalala': 3}
  myString = json.dumps(jsonObjekts)
  print (myString)

def fromJSON():
  print("Python variables: ")
  python_dict =  {"vards": "Davis", "gadi": 16, "Klase":"11"}
  python_list =  ["Viens", "Divi", "Tris"]
  python_str =  "Python Json"
  python_int =  (1234)
  python_float =  (21.34)
  python_T =  (True)
  python_F =  (False)
  python_N =  (None)

  json_dict = json.dumps(python_dict)
  json_list = json.dumps(python_list)
  json_str = json.dumps(python_str)
  json_num1 = json.dumps(python_int)
  json_num2 = json.dumps(python_float)
  json_t = json.dumps(python_T)
  json_f = json.dumps(python_F)
  json_n = json.dumps(python_N)

  print("json dict : ", json_dict)
  print("jason lists : ", json_list)
  print("json strings : ", json_str)
  print("json numurs1 : ", json_num1)
  print("json numurs2 : ", json_num2)
  print("json true : ", json_t)
  print("json false : ", json_f)
  print("json null ; ", json_n)

def toJSON():
  print("JSON: ")
  jobj_dict =  '{"name": "David", "age": 6, "class": "I"}'
  jobj_list =   '["Red", "Green", "Black"]'
  jobj_string = '"Python Json"'
  jobj_int = '1234'
  jobj_float =  '21.34'
  python_dict =  json.loads(jobj_dict)
  python_list = json.loads(jobj_list)
  python_str =  json.loads(jobj_string)
  python_int =   json.loads(jobj_int)
  python_float = json.loads(jobj_float)

  print("Python dictionary: ", python_dict)
  print("Python list: ", python_list)
  print("Python string: ", python_str)
  print("Python integer: ", python_int)
  print("Python float: ", python_float)