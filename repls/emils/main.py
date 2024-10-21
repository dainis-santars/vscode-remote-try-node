import random
e = 0
m = 0
i = 0
l = 0
while e < 9:
  s = random.choice(['cipars', 'ģērbonis'])
  m += 1
  e += 1
  if s == 'ģērbonis':
   i += 1
   print (m,". metiens : ģērbonis")
  if s == 'cipars':
    l += 1
    print (m,". metiens : cipars")
print ("cipars",l,"reizes" )
print ("ģērbonis",i, "reizes")
if i > l :
  print ("uzkrīt ģērbonis vairākas reizes!")
elif l > i :
  print ("uzkrīt cipars vairākas reizes!")