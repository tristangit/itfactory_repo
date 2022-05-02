'''#if else reprezinta practic niste operatori logici unde doar unul din ei poate fi adevarat

#Verifica si afiseaza daca x este numar pozitiv sau nu
numar = int(input())
if numar>0:
    print('Numarul este pozitiv')
else:
    print('Numarul nu este pozitiv')'''


'''#Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
numar = int(input())
if numar>0:
    print('Numarul este pozitiv')
elif numar<0:
    print('Numarul este negativ')
else:
    print('Numarul este neutru')'''

''''#Verifica si afiseaza daca x este intre -2 si 13
x = int(input())
if x>=-2 and x<=13:
    print(x)'''

'''#Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
x = int(input('Numarul : '))
y = int(input('Numarul : '))
scadere = x-y
if scadere < 5:
    print(scadere)'''

'''#Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
x = int(input('Numar : '))
if not(x>=5 and x<=27):
    print(x)'''


'''#Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
#x si y (int)
x = int(input('Numar : '))
y = int(input('Numar : '))
if x==y:
    print('x = y')
elif x>y:
    print(x)
elif x<y:
    print(y)'''


'''#x, y, z - laturile unui triunghi
#Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
x = int(input())
y = int(input())
z = int(input())
if x==y and not(y==z):
    print('Triunghiul este isoscel')
elif x==z and not(x==y):
    print('Triungiul este isoscel')
elif y==z and not(x==z):
    print('Triungiul este isoscel')
elif x==y and y==z:
    print('Triunghiul este echilateral')'''


'''#Citeste o litera de la tastatura
#Verifica si afiseaza daca este vocala sau nu
x = str(input('Litera : '))
if (x == 'a' or x == 'e' or x == 'i' or
        x == 'o' or x == 'u' or x == 'A' or
        x == 'E' or x == 'I' or x == 'O' or
        x == 'U'):
		print('Litera este vocala')
else:
		print('Litera este consoana')'''


'''#Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
#Peste 9 => A
#Peste 8 => B
#Peste 7 => C
#Peste 6 => D
#Peste 4 => E
#4 sau sub => F
nota = float(input('Nota : '))
if nota>9:
	print('A')
elif nota>8 and nota<9:
	print('B')
elif nota>7 and nota<8:
	print('C')
elif nota>6 and nota<7:
	print('D')
elif nota>4 and nota<6:
	print('E')
elif nota<4 and nota>0:
	print('F')'''


'''#Verifica daca x are minim 4 cifre
numar = str(input("Introdu un numar din 4 cifre: "))
if len(numar)>=4 and numar.isdigit():
	print('Este corect')
else:
	print('Nu este corect')'''


'''#Verifica daca x are exact 6 cifre
numar = str(input("Introdu un numar: "))
if len(numar)==6 and numar.isdigit():
	print('Corect')
else:
	print('False')'''


'''#Verifica daca x este numar par sau impar
numar = int(input('Numar : '))
if (numar % 2) == 0:
	print('Numarul este par')

else:
	print('Numarul este impar')'''


'''#x, y, z (int)
#Afiseaza care este cel mai mare dintre
x = float(input('Numar : '))
y = float(input('Numar : '))
z = float(input('Numar : '))

if (x>y) and (x>z):
	mai_mare = x
elif (y>x) and (y>z):
	mai_mare = y
else:
	mai_mare = z

print("Cel mai mare este:", mai_mare)'''


#x, y, z - reprezinta unghiurile unui triunghi
#Verifica si afiseaza daca triunghiul este valid sau nu
x = int(input('Unghi A: '))
y = int(input('Unghi B: '))
z = int(input('Unghi C: '))
w = x+y+z

if w==180:
	print("Este triunghi")
else:
	print("Nu este triunghi")




















