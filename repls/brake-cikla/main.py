r = 0
print("Mini mīklu!\nKas bez un bez dēļiem uztaisa tiltu?") # \n ir jauna rinda
while r < 100: # kamēr r mazāks nekā 100
  a = input("Atbilde: ")
  a = a.lower()
  r += 1
  if a == "ziema":
    break
  print("Mini vēl!")
print("Jā! Pareizi!")
print("Mēģinājumu skaits:",r)

s = 0
print("Ievadi skaitļus! Ja apnika, raksti B")
while s < 1000:
  z = input("Skailtis: ")
  print(z)
  if z == "B":
    break