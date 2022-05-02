# Usor (recomandat)
# 1. Revizualizeaza intalnirea 5 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Functii din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 7 despre OOP din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/
#
# Pentru toate exercitiile
# Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
# Daca functia are return, printati raspunsul
#
# b. Dificultate: usor spre mediu
#
# 1. Functie care sa calculeze si sa returneze suma a 2 numere

# print ('============================= Solutie ============================')
# def f(x,y):
#     print(x + y)
#
# x = int(input("Introduceti numar: "))
# y = int(input("Introduceti numar: "))
# print(x+y)
# print ('============================= Solutie ============================')

#
# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
# print ('============================= Solutie ============================')
#
# def f(z):
#     if z%2 == 0:
#         print(f'True')
#     # elif:
#     #     z == 0
#     #         numar = 0
#     else:
#         print(f'False')
#     return False
#
# z = int(input('Introduceti numar :'))
# numar = f(z)
#
# print ('============================= Solutie ============================')

#
# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)

# print ('============================= Solutie ============================')
# def f(l):
#     print(len(l))
#
# nume = input('Nume:')
# prenume = input('Prenume:')
# nume_mijlociu = input('Al 2 lea prenume: ')
# l = nume + prenume + nume_mijlociu
# print (f(l))
# print ('============================= Solutie ============================')
#
# 4. Functie care returneaza aria dreptunghiului
#
# print ('============================= Solutie ============================')
# def aria_dreptunghiului(latime,lungime):
#     aria = latime * lungime
#     return aria
#
# latime = int(input('Latime: '))
# lungime = int(input('Lungime: '))
# print(aria_dreptunghiului(latime,lungime))
# print ('============================= Solutie ============================')


#
# 5. Functie care returneaza aria cercului

# print ('============================= Solutie ============================')
# def aria_cercului(r):
#     PI = 3.14
#     return PI * (r*r)
#
# r = int(input('Introduceti raza: '))
# print(aria_cercului(r))
# print ('============================= Solutie ============================')

#
# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. False daca nu

# print ('============================= Solutie ============================')
# def f(char):
#     if char in string:
#         print(True)
#     else:
#         return print(False)
#
# string = 'unu doi trei'
# char = 'x'
# f(char)
# print ('============================= Solutie ============================')


# 7. Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y

# print ('============================= Solutie ============================')
# def string_count(s):
#     d={"upper":0, "lower":0}
#     for y in s:
#         if y.isupper():
#            d["upper"]+=1
#         elif y.islower():
#            d["lower"]+=1
#         else:
#            pass
#     print ("Input string : ", s)
#     print ("Nr de caractere lower este: ", d["lower"])
#     print ("Nr de caractere upper este: ", d["upper"])
#
# string_count('Unu Doi Trei BlA Bla')
# print ('============================= Solutie ============================')

# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
#
# 9. Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.
#
# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
#
#
# c. Optionale (may need google)
#
# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna
#
# 12. Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere
#
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
#
# 13. Functie care primeste o lista de cifre (adica doar 0-9)
# Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un DICT care ne spune de cate ori apare fiecare litera
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
#
# 14. Functie care primeste 3 numere
# Returneaza valoarea maxima dintre ele
#
# 15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3
# Suma va fi 6 (0+1+2+3)
#
# BONUS:
#
# 16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
# ‘Numele este de baiat’ sau ‘Numele este de fata’
#
#
# 17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
# Returnati numerele comune
#
# Ex:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Raspuns: {2, 3}
#
# 18. Functie care sa aplice o reducere de pret
# Daca produsul costa 100 lei si aplicam reducere de 10%
# Pretul va fi 90
# Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
#
# 19. Functie care sa afiseze data si ora curenta
#
# 20. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)
