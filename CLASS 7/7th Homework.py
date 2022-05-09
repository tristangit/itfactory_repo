# 1.Git setup
#
# OBLIGATORIU!
# Git setup: (ne ajuta sa ne expunem proiectele angajatorilor - super important)
# https://drive.google.com/file/d/1yaURoa2VGyCARQ7BUZ-gplnMTxnJjRuz/view?usp=sharing
#
# OPTIONAL
# How to use gitignore: (ne ajuta sa ignoram fisiere pe care nu vrem sa le expunem)
# https://drive.google.com/file/d/17NVuy28nspPt5_DzynmD0CF7mbmiVzY9/view?usp=sharing
#
#
# 2. Faceti exercitiul dupa ce ati urcat proiectul (tot ce am facut pana acum impreuna)
#
# ABSTRACTION
# Clasa abstracta FormaGeometrica
# Contine un field PI=3.14
# Contine o metoda abstracta aria
# Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
#
# INHERITANCE
# Clasa Patrat - mosteneste FormaGeometrica
# constructor pt latura
# ENCAPSULATION
# latura este proprietate privata
# Implementati getter, setter, deleter pt latura
# Implementati metoda ceruta de interfata
#
# Clasa Cerc - mosteneste FormaGeometrica
# constructor pt raza
# raza este proprietate privata
# Implementati getter, setter, deleter pt raza
# Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte
# POLYMORPHISM
# Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
#
#
# Creati un obiect de tip Patrat si jucati-va cu metodele lui
# Creati un obiect de tip Cerc si jucati-va cu metodele lui
#

print('================== Solutie =======================')
from abc import abstractmethod
class FormaGeometrica:
    pi = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')

#Pentru clasa patrat
print('===================== Patrat ====================')

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        a = self.__latura**2
        return a

    def get_latura(self):
        return self.__latura

    def set_latura(self, valoare_noua):
        if valoare_noua > 0:
            self.__latura = valoare_noua
        else:
            print('Nu poti seta o latura cu valoare negativa!')

    def del_latura(self):
        print('Am sters latura!')
        self.__latura = None


p1 = Patrat(10)
print(p1.aria())

print(p1.get_latura())

p1.set_latura(-15)
print(p1.get_latura())

print(p1.del_latura())

print('===================== Patrat ====================')

#Pentru clasa Cerc
print('===================== Cerc ====================')

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        #pi = 3.14
        a = self.pi*(self.__raza**2)
        return a

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza_noua):
        if raza_noua > 0:
            self.__raza = raza_noua
        else:
            print('Nu poti avea o raza cu valoare negativa!')

    def del_raza(self):
        print('Am sters raza!')
        self.__raza = None

    def descrie(self):
        print('Nu am colturi!')

c1 = Cerc(10)
print(c1.aria())

print(c1.get_raza())

c1.set_raza(20)
print(c1.get_raza())

print(c1.del_raza())

c1.descrie()

# 3. Actualizati proiectul pe github facand un push la noul cod
# In Folder de teme ajunge sa puneti doar linkul cu proiectul vostru public
