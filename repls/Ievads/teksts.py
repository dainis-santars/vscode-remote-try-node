def parisNeparis():
  ievadsSklaitlis = int(input("Ievadiet skaitli:"))
  paris = (ievadsSklaitlis % 2) == 0
  if paris == True:
    print("Skaitlis {} ir Pāra skaitlis".format(ievadsSklaitlis))
  else:
    print("Skaitlis {} ir Nepāra skaitlis".format(ievadsSklaitlis))
