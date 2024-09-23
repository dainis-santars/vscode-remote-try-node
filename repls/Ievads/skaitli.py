def sumaVai3(x, y, z):
  sum = x + y + z
  if x == y == z:
    sum = sum * 3
  return sum

def salidzinatViegli():
  print(2==2)
  print(2!=3)
  print(2<3)
  print(3<=2)
  print(2 in [1,2,3])

def salidzinat():
  saraksts_1 = set(["Balts", "Melns", "Sarkans"])
  saraksts_2 = set(["Sarkans", "Zals"])
  print("Originalie elementi:")
  print(saraksts_1)
  print(saraksts_2)
  print("\nKrasas kas ir saraksts_1 un nav sarakst_2:")
  print(saraksts_1.difference(saraksts_2))
  print("\nKrasas kas ir saraksts_2 un nav sarakst_1:")
  print(saraksts_2.difference(saraksts_1))

def zars():
  diena = 21
  if diena == 20:
	  print("Nododiet mājasdarbus!")
  elif diena == 21:	
    print("Kursu diena!")
  else:
    print("Strādājam pie jaunā mājas darba!")

def lode():
  pi = 3.1415926535897931
  r = 6.0
  V = 4.0 / 3.0 * pi * r**3
  print('The volume of the sphere is: ', V)

def dzddatums():
  diena = 21
  if diena == 25:
	  print("Dzimšanas diena Dainim")
  elif diena == 28:	
    print("Dzimšanas diena Andrim")
  else:
    print("Strādājam pie jaunā mājas darba!")