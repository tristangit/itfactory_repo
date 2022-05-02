#O variabila reprezinta o metoda de stocare a unui caracter sau sir de caractere / expresii

#Definire si initializare variabile
a = 'Salutare'
b = 4
c = 4.69
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(f"=======================================================")

#Folosire functia round si afisare
c = round(4.69)
print(c)

print(type(c))

print(f"=======================================================")

#Propozitii

print(b+c)
print(f"{a} {b} {c} {d}")
print(a + " " + str(b))
print(f"{a} am {b} mere {d}")

print(f"=======================================================")

#Citire de la tastatura, use lenght
nume = "Popa "
prenume = "George Viorel"
nume_complet = nume + prenume

print(nume_complet)
print(len(nume_complet))

print(f"=======================================================")
#Aria dreptunghiului
lungimea = 4
latimea = 6
aria = lungimea * latimea
print(aria)
print(f"Aria dreptunghiului este {aria}")

print(f"=======================================================")

string = "Coral is either the stupidest animal or the smartest rock"
#print(len(string))
print(string[:-7])

#print(string[:5])
#print(string[-5:])
string1 = string[:5] + string[-5:]
print(string1)

find_the = string.count("the")
print(find_the)

upper_the = string.replace("the", "THE")
print(upper_the)

string2 = string.index("rock")
print(string2)
print(string[:53])

print(f"=======================================================")

#A 5 a variabila
e = a + str(b) + str(c) + str(d)
print(e)


print(f"=======================================================")

str1 = "0123456789"
print("Even Characters:", str1[::2]) # Characters at even index
print("Odd Characters:", str1[1::2]) # Characters at odd index

