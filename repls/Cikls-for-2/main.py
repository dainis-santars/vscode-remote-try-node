import random
k = ["Pūciņš","Ņauris","Skrāpis"]
uzbuve = ["kārns","apaļīgs","tukls"]
for kakis in k:
  u = random.choice(uzbuve)
  print(kakis,"ir",u)