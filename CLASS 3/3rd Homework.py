#Declara o lista
arpegiu = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]

#Afisare
print(arpegiu)

#Inverseaza, suprascrie si afiseaza lista
arpegiu = arpegiu[::-1]

print(arpegiu)

#Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat) + print
print(arpegiu[-1:-9:-1])

#De cate ori apare ‘do’?
print(arpegiu.count("do"))

#Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
#Gasiti 2 variante sa le uniti intr-o singura lista.
ls1 = [3, 1, 0, 2]
ls2 = [6, 5, 4]

for i in ls2:
    ls1.append(i)
print(ls1)

#sau
ls1 = [3, 1, 0, 2]
ls2 = [6, 5, 4]
ls3 = ls1 + ls2
print(ls3)


#Sortati si afisati lista generata la ex anterior
#Stergeti numarul 0 folosind o functie
#Afisati iar lista
ls3.sort()
print(ls3)

if 0 in ls3:
    ls3.remove(0)
print(ls3)

print('================================================================')
#Folosind un if verificati lista generata la ex3 si afisati
#Lista este goala
#Lista nu este goala
ls3 = []
ls1 = [3, 1, 0, 2]
ls2 = [6, 5, 4]
ls3 = ls1 + ls2
print(ls3)

if len(ls3) > 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')

#Folositi o functie care sa stearga lista de la ex3

for x in ls1:
    ls3.remove(x)
for y in ls2:
    ls3.remove(y)
print(ls3)

if len(ls3) > 0:
    print('Lista nu este goala')
else:
    print('Lista este goala')

print('================================================================')
#Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
#Folositi o functie ca sa afisati Elevii (cheile)
elevi = ['Ana', 'Gigel', 'Dorel']
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}

for x in elevi:
    if x=='Ana':
        print(f"{x} nota {dict1['Ana']} ")
    elif x=='Gigel':
        print(f"{x} nota {dict1['Gigel']} ")
    elif x=='Dorel':
        print(f"{x} nota {dict1['Dorel']} ")

#Dorel a facut contestatie si a primit 6
#Modificati nota lui Dorel in 6
#Printati nota dupa modificare

dict1.update({'Dorel' : 6})
for x in elevi:
    if x=='Ana':
        print(f"{x} nota {dict1['Ana']} ")
    elif x=='Gigel':
        print(f"{x} nota {dict1['Gigel']} ")
    elif x=='Dorel':
        print(f"{x} nota {dict1['Dorel']} ")


# Gigel se transfera din clasa
# Cautati o functie care sa il stearga
# Vine un coleg nou. Adaugati Ionica, cu nota 9
# Printati noii elevi
del dict1["Gigel"]
dict1['Ionica'] = 9
elevi = ['Ana', 'Dorel', 'Ionica']
print(elevi)
print(dict1)

print('======================================================')

# Adaugati in zilele_sapt ‘luni’
# Afisati zile_sapt

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

zile_sapt.add('luni')
print(zile_sapt)

# Folositi un if si verificati daca
# Weekend este un subset al zilelor din sapt
# Weekend nu este un subset al zilelor din sapt

if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din sapt')
else:
    print('Weekend nu este un subset al zilelor din sapt')

#Afisati diferentele dintre aceste 2 seturi
print(zile_sapt.difference(weekend))
print(weekend.difference(zile_sapt))

#Afisati intersectia elementelor din aceste 2 seturi
print(zile_sapt & weekend)
print(weekend.intersection(zile_sapt))

print('====================== OPTIONAL ===========================')

# Ne imaginam o echipa de fotbal pt teren sintetic.
# 3 Schimbari maxime admise
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
# Schimbari_max = 3
#
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# Efectuam schimbarea
# Stergem jucatorul scos din lista
# Adaugam jucatorul intrat
# Afisam a intrat x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Afisati ‘mai aveti z schimbari’
#
# Testati codul cu diferite valori

# lot = ['Hagi', 'Lacatus', 'Prodan', 'Galca', 'Mutu']
# jucatori_teren = ['Hagi', 'Prodan', 'Galca']
# rezerve = ['Lacatus', 'Mutu']
# schimbari_efectuate = 2
# schimbari_max = 3
#
# for x in range(len(jucatori_teren)):
#     print(jucatori_teren[x])














