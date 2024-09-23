import re
txt = '''Reiz viens zvejnieks ved regavās zivis no upes. Lapsa ceļmalā jūt zivu smaku un viņai ar' iekāris zivu gaļas. Viņa aizskrien ar riņķi zvejniekam priekšā, nogulstas uz ceļa un izliekas par nosprāgušu. Zvejnieks tur dabrauc un redz: lapsa nosprāgusi. Viņš paņem lapsai pie astes, uzsviež uz vezuma un pārdomā: "Mājā varēs nomaukt ādu." Zvejnieks nu brauc priecīgs uz māju, bet lapsa tikai kārna zivis no vezuma laukā. Izsviedusi visas zivis, lapsa klusītēm nolec no vezuma un aizbēg. Zvejnieks pārbrauc mājā un grib palielīties par savu lielo lomu, bet paskatās — ne vair zivu, ne lapsas!'''
# print(txt)
reiz = re.match(r'Reiz', txt)
if reiz is not None:
  print('Pasaka sākas ar "Reiz".')
else:
  print('Pasaka nesākas ar "Reiz".')
lapsa = re.findall(r'lapsa', txt)
print('Vārds "lapsa" pasakā sastopams',len(lapsa),'reizes')
a = re.findall(r'\b[a,A]\w+', txt)
print(len(a), 'vārdi pasakā sākas ar burtu "a" vai "A"')
garums4 = re.findall(r'\b\w{4}\b', txt)
print('Četrus burtus gari vārdi ir:')
for i in garums4:
  print(i)
garums8 = re.findall(r'\b\w{8,}\b', txt)
print('Vismaz 8 burtus gari vārdi ir:')
for i in garums8:
  print(i)
#ai, au, ie, ei, ui, iu, oi, ou
ds = re.findall(r'\w*ai\w*|\w*au\w*|\w*ie\w*|\w*ei\w*|\w*ui\w*|\w*iu\w*|\w*oi\w*|\w*ou\w*', txt)
print('Vārdi ar divskaņiem:')
for i in ds:
  print(i)