# Recomandat (usor)
# 1. Revizualizeaza intalnirea 6 si ia notite in caz ca ti-a scapat ceva
#
# b. Obligatorii (mediu)
#
# Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei
#
# 1.
# Clasa Cerc
#
# Atribute: raza, culoare
#
# Constructor pt ambele atribute
#
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

# print('============================= Solutie ============================')
#
#
# class Cerc:
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descrie_cerc(self):
#         print(f'Cercul {self.culoare} are raza {self.raza}')
#
#     def aria(self):
#         from cmath import pi
#         a = pi * self.raza**2
#         return a
#
#     def diametru(self):
#         d = 2 * self.raza
#         return d
#
#     def circumferinta(self):
#         from math import pi
#         c = 2 * pi * self.raza
#         return c
#
#
# cerc1 = Cerc(4, 'Rosu')
# cerc2 = Cerc(5, 'Albastru')
# cerc1.descrie_cerc()
# cerc2.descrie_cerc()
#
# print(cerc1.aria())
# print(cerc2.aria())
#
# print(cerc1.diametru())
# print(cerc2.diametru())
#
# print(cerc1.circumferinta())
# print(cerc2.circumferinta())
#
#
#
# print('============================= Solutie ============================')

# 2.
# Clasa Dreptunghi
#
# Atribute: lungime, latime, culoare
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie
#atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().

# print('============================= Solutie ============================')
#
# class Dreptunghi:
#     def __init__(self, culoare, latime, lungime):
#         self.culoare = culoare
#         self.latime = latime
#         self.lungime = lungime
#
#     def descrie(self):
#         print(f'Dreptunghiul {self.culoare} are lungimea {self.lungime} si latimea {self.latime}')
#
#     def aria_d(self):
#         ad = self.lungime * self.latime
#         return ad
#
#     def perim_d(self):
#         perim_d = 2 * (self.lungime + self.latime)
#         return perim_d
#
#     def schimba_culoare(self, noua_culoare):
#         self.culoare = noua_culoare
#
# dreptunghi1 = Dreptunghi("rosu", 10, 7)
# dreptunghi2 = Dreptunghi("albastru", 12, 9)
# dreptunghi1.descrie()
# dreptunghi2.descrie()
#
# print(dreptunghi1.aria_d())
# print(dreptunghi2.aria_d())
#
# print(dreptunghi1.perim_d())
# print(dreptunghi2.perim_d())
#
#
# dreptunghi1.descrie()
# dreptunghi1.schimba_culoare('verde')
# dreptunghi1.descrie()
#
# dreptunghi2.descrie()
# dreptunghi2.schimba_culoare('siclam')
# dreptunghi2.descrie()
#
#
#
# print('============================= Solutie ============================')
# 3.
# Clasa Angajat
#
# Atribute: nume, prenume, salariu
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)

# print('============================= Solutie ============================')
#
# class Angajat:
#     def __init__(self,nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         print(f'Salariatul {self.nume} {self.prenume} are salariul de {self.salariu}')
#
#     def salariu_anual(self):
#         sal_an = self.salariu * 12
#         return sal_an
#
#     def marire_salariu(self, procent):
#         self.procent = procent
#         marire = self.procent / 100 * self.salariu
#         salariu_actualizat = self.salariu + marire
#
#         return f'Salariatului {self.nume} {self.prenume} i-a fost marit salariul cu {marire} avand in acest moment salariul de: {salariu_actualizat}'
#
#
# salariat1 = Angajat("Popa", "George", 5000)
# salariat1.descrie()
# salariat2 = Angajat("Popescu", "Ion", 4000)
# salariat2.descrie()
#
# print(salariat1.salariu_anual())
# print(salariat2.salariu_anual())
#
# print(salariat1.marire_salariu(10))
# print(salariat2.marire_salariu(15))
#
# print('============================= Solutie ============================')


# 4.
# Clasa Factura
#
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
#
# Constructor: toate atributele, fara serie
#
# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti
#
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total
# Telefon |      7       |       700       | 49000
#
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
#

# print('============================= Solutie ============================')

# class Factura:
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     # def descrie(self):
#     #     print(f'Factura {self.numar} pentru produsul {self.nume_produs} pentru cantitatea {self.cantitate} \n'
#     #           f'la pret per bucata de {self.pret_buc} a fost generata')
#     #
#     # def schimba_cantitatea(self, noua_cantitate):
#     #     self.cantitate = noua_cantitate
#
#     def gen_factura(self):
#         import time
#         contor = str(f'Seria : FF \n'
#                      f'Numar : {self.numar}')
#         total = self.pret_buc * self.cantitate
#         print(contor)
#         data = time.localtime()
#         print(f'{data.tm_mday}-{data.tm_mon}-{data.tm_year} {data.tm_hour}:{data.tm_min}:{data.tm_sec}')
#         print("\n\n")
#         print('_______________________________________________')
#         print(" |  Produs  | cantitate | pret bucata | Total |")
#         print('_______________________________________________')
#         print(f' | {self.nume_produs}  |    {self.cantitate}     |     {self.pret_buc}    | {total}  |')
#         print('_______________________________________________')
#
#
# factura1 = Factura(1, "telefon", 10, 1000)
# factura2 = Factura(2, "tableta", 20, 800)
# # factura1.descrie()
# # factura2.descrie()
# # #
# # factura1.schimba_cantitatea(20)
# # factura1.descrie()
# # factura2.schimba_cantitatea(50)
# # factura2.descrie()
#
# factura1.gen_factura()
# factura2.gen_factura()
#
#
#
# print('============================= Solutie ============================')

# 5.
# Clasa Cont
#
# Atribute: iban, titular_cont, sold
#
# Constructor pentru toate
#
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)

print('============================= Solutie ============================')
#
class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def consultare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold}')

    def debitare_cont(self):
        debit = int(input("Introduceti suma pe care doriti sa o depuneti: "))
        self.sold = debit + self.sold
        return self.sold

    def creditare_cont(self):
        credit = int(input("Introduceti suma pe care doriti sa o retrageti: "))
        self.sold = self.sold - credit
        return self.sold


persoana1 = Cont("RO04BRDE0000000001", "George Popa", 10000)
persoana2 = Cont("RO04BRDE0000000002", "Ion Popescu", 15000)

persoana1.consultare_sold()
persoana2.consultare_sold()

print(persoana1.debitare_cont())
persoana1.consultare_sold()
print(persoana2.debitare_cont())
persoana2.consultare_sold()

print(persoana1.creditare_cont())
persoana1.consultare_sold()
print(persoana2.creditare_cont())
persoana2.consultare_sold()


print('============================= Solutie ============================')

# BONUS: (daca aveti timp si doriti sa lucrati suplimentar)

# 6.
# Clasa Masina
#
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate masinile cand ies din fabrica sunt gri
# Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
# Culori disponibile = alegeti voi 5-7 culori
# Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
# Inmatriculata = False
#
# Constructor: model, viteza_maxima
#
# Metode:
# descrie() (se vor printa toate atributele, inafara de culori_disponibile)
# inmatriculare() - va schimba atributul inmatriculata in True
# vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
# accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
# franeaza() - masina se va opri si va avea viteza 0
