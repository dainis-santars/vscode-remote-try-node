def pareizsLaiks():
  import datetime
  now = datetime.datetime.now()
  print ("Šodienas Laiks un Datums ir : ")
  print (now.strftime("%d-%m-%Y %H:%M:%S"))