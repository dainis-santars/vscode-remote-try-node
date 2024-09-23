from heapq import nlargest
import json

# Vārdnīcas
def atzimes():
  d = {'Janis': 6, 'Anna': 5, 'Marta': 9} 
  for dict_key, dict_value in d.items():
    print(dict_key,'->',dict_value)

def pievienotAtzimi():
  atzimes = {'Janis': 6, 'Anna': 5, 'Marta': 9}
  print(atzimes)
  atzimes.update({'Maris': 10})
  print(atzimes)

def augstakasAtzimes3():
# from heapq import nlargest - vajag izpildei
  my_dict = {'Janis': 6, 'Anna': 5, 'Marta': 9,'Jekabs': 7, 'Arnis': 4, 'Kaija': 8}  
  three_largest = nlargest(3, my_dict, key=my_dict.get)
  print(three_largest) 

#Saraksts

def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max

def apvienoSarakstus():
  list1 = [1, 2, 3, 0]
  list2 = ['Red', 'Green', 'Black']
  final_list = list1 + list2
  print(final_list)

def navdubulta():
  a = [10,20,30,20,10,50,60,40,80,50,40]

  dup_items = set()
  uniq_items = []
  for x in a:
      if x not in dup_items:
          uniq_items.append(x)
          dup_items.add(x)

  print(a)
  print(dup_items)
  print(uniq_items)

def izvadaSarakstus():
  saraksts=["tipsis","topsis","tedis","muris"]
  for i in saraksts:
    print(i)
  si = input("kas: ")
  if si not in saraksts:
    saraksts.append(si)
  print(saraksts)

def pievienotRezultatu():
  top = {'Janis': 6, 'Anna': 5, 'Marta': 9,'Jekabs': 7, 'Arnis': 4, 'Kaija': 8}
  print(top)
  top.update({'Harrijs' : 90})
  print(top)

def saglabatDatus():
  top = {'Janis': 6, 'Anna': 5, 'Marta': 9,'Jekabs': 7, 'Arnis': 4, 'Kaija': 8}
  with open('jaunais.json', 'w') as f:
    json.dump(top, f, indent=4)