import time
from termcolor import colored
import random

# Nejauši izvēlas sveicienu un padara to treknu
sveicinasanas_veidi = random.choice(["Čau!", "Hei!", "Sveiks!"])
print("\033[1m" + sveicinasanas_veidi + "\033[0m")

# Aizkavē nākamo tekstu par 1.125 sekundēm un padara skaitli 10 treknu, lai to izceltu
time.sleep(1.125)
print("\nVai esi spēgīgs atminēt šīs" + "\033[1m" + " 10 " + "\033[0m" + "latviešu tautas mīklas? Izmēģini pats un izaicini sevi! :)\n")

# Mainīgais "punkti" nosaka sākuma punktu skaitu
punkti = 0
minejumu_skaits = 0
# Aizkavē nākamo tekstu par 3 sekundēm
time.sleep(3)
# Tiek uzkrātas visas mīklas ar saskaņotām atbildēm
miklas = {
  "Kam ir dzelzs mēle?":"Zvanam",
  "Galva no dzelzs, kājas no koka.":"Āmurs",
  "Četri viena tēva bērni, cits no cita ātri bēg.":"Gadalaiki",
  "Kam nevar pāri pārkāpt?":"Ēnai",
  "Iet ūdenī sarkans, iznāk melns.":"Ogle",
  "Kad uz mutes, tad pilna, kad augšpēdus, tad tukša.":"Cepure",
  "Ne kāju, ne roku, bet uz priekšu iet.":"Čūska",
  "Septiņjūdžu plata josta, katra jūdze savā krāsā.":"Varavīksne",
  "Divas māsiņas abpus kalna.":"Ausis",
  "Kas runā visās pasaules valodās?":"Atbalss"
}

# print(miklas)
# izdrukā vārdnīcu
# print("\n\n\n")

keys = list(miklas.keys())
random.shuffle(keys)

miklasSajaukts = dict()
for key in keys:
  miklasSajaukts.update({key: miklas[key]})

# print(miklasSajaukts)
# izdrukā sajauktā vārdnīcu

for k in miklasSajaukts.keys():
  print(k)
  minejumu_skaits += 1
  atbilde = input("Ievadi atbildi: ")
  if atbilde == miklasSajaukts[k]:
    print("Pareizi!")
    punkti += 1
  else:
    print("Nepareizi!")
    print("Pareizā atbilde:","\033[1m"+ miklasSajaukts[k]+"\033[0m")


# Tiek izveidots nosacījums, kas parāda iznākumu un tekstu lietotājam, ja viņš  atbild pareizi uz nevienu mīklu
if punkti == 0:
  print("Tu atbildēji pareizi uz" + "\033[1m" + " NEVIENU " + "\033[0m" + "mīklu. Es biju labākās domās par tevi.😭")
# Tiek izveidots nosacījums, kas parāda iznākumu un tekstu lietotājam, ja viņš  atbild pareizi uz 1 mīklu
elif punkti == 1:
  print("Tu atbildēji pareizi uz",punkti,"mīklu no 10. Kā tad tā???😣")
  # Tiek izveidots nosacījums, kas parāda iznākumu un tekstu lietotājam, ja viņš  atbild pareizi uz 2 - 3 mīklām. Punktu skaitam 1 - 3 teksts ir vienāds, bet rakstu atsevišķi, lai sakrīt pareiza gramatika ar vienskaitli
elif punkti >= 2 and punkti <= 3:
  print("Tu atbildēji pareizi uz",punkti,"mīklām no 10. Kā tad tā???😣")
# Tiek izveidots nosacījums, kas parāda iznākumu un tekstu lietotājam, ja viņš  atbild pareizi uz 4 - 6 mīklām
elif punkti > 3 and punkti <= 6:
  print("Tu atbildēji pareizi uz",punkti,"mīklām no 10. Varēja būt labāk, bet varēja būt arī sliktāk.😐")
# Tiek izveidots nosacījums, kas parāda iznākumu un tekstu lietotājam, ja viņš  atbild pareizi uz 7 - 9 mīklām
elif punkti > 6 and punkti <= 9:
  print("Tu atbildēji pareizi uz",punkti,"mīklām no 10. Tu esi ļoti spēcīgs mīklu eksperts!😄")
  # Tiek izveidots nosacījums, kas parāda iznākumu un tekstu lietotājam, ja viņš atbild pareizi uz visām mīklām
elif punkti == 10:
  print("Tu atbildēji pareizi uz" + "\033[1m" + " VISĀM " + "\033[0m" + "10 mīklām. Tagad tu oficiāli esi mīklu dievs, URRĀĀĀĀĀ!!!!!🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")

# Punkti iedalās šādās kategorijās: 0; 1 - 3; 4 - 6; 7 - 9; 10