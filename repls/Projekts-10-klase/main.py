import random
skolens = ["Baranovska Sofija","Bucis Ernests Gints","Da Košta-Loreiru Aleksandru Gabriels","Dmitrijevs Eduards","Duļķis Emīls","Ezeriņa Patrīcija Paula","Folkmanis Jānis","Garkuļs-Gurevičs Rolands","Graumane Linda","Greiškāns Kristers","Klaramunts-Antila Nikolass","Kode Zaiga","Kronberga Kate","Linde Estere","Makruzova Una Everita","Skuja Kitija","Šalna Linda","Teļatņikovs Iosifs"]
dzimums = ['sieviete','vīrietis']
edu = ['mācās augstskolā klātienē','mācās augstskolā neklātienē','vidējā','vidējā profesionālā','augstākā profesionālā','augstākā','maģistra grāds']
intr = ['apmeklē interešu izglītības kursus', '-', 'mācās online kursos']
statuss = ['prec.','neprec.']
#berni = ['nav','ir']
vieta = ['lauki','ciemats','mazpilsēta','lielā pilsēta','Rīga']
auto = ['Ir','Nav']
marka = ['Audi','BMW','Citroen','Ford','Mercedes','Opel','Renault','Toyota','Volkswagen','Volvo']
darbs = ['strādā sev','strādā citam','nestrādā']
for i in skolens:
  print(i)
  print('Tava iedomātā lietotāja dati')
  print('Dzimums:',random.choice(dzimums))
  a = random.randint(20,30)
  print('Vecums pilnos gados:',a)
  print('Iegūtā izglītība:',random.choice(edu))
  print('Intereses: ', random.choice(intr))
  print('Nodarbinātība:',random.choice(darbs))
  print('Ģimenes stāvoklis:',random.choice(statuss))
  b = random.randint(1,4)
  #c = random.choice(berni)
  #print('Bērni',c)
  #if c != 'nav':
  #  print('Skaits:',b)
  print('Dzīvesvieta:',random.choice(vieta))
  d = random.choice(auto)
  print(d,'auto', end="")
  if d != 'Nav':
    print(' un tas ir',random.choice(marka))
  print('\n')