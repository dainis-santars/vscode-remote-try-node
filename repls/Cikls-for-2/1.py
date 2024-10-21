sum = 0
nsum = 0
kn = 0
x = [1,3,6,22,13,7,37,4]
print(x)
for i in x:
  sum = sum + i
  kn = kn + 1
  if i % 2 != 0:
    nsum = nsum + i
  if i == 7:
    print("7 ir",kn,". vieta sarakstā")
print("Visu skaitļu summa ir",sum)
print("Nepāra skaitļu summa ir",nsum)