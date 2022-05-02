class Car:

    def __init__(self, brand, year, color):
        self.__brand = brand
        self.__year = year
        self.__color = color

    def get_color(self):
        return self.__color

    # vopseaua unei masini se mai poate modifica ulterior
    def set_color(self, new_color):
        self.__color = new_color

    # Atentie: brand si year NU se mai modifica!!!
    def get_brand(self):
        return self.__brand

    def get_year(self):
        return self.__year


c1 = Car("toyota", 2012, "red")

# eu accesez atributul color din afara clasei (din programul principal)
# ceea ce nu este chiar ok dpdv al principiilor OOP
# Incapsulare: eu, din prog principal, sa nu mai am acces direct la color din c1,
# ci sa obtin color prin intermediul unui "getter" (aka o metoda din clasa Car care imi returneaza color)
#print(c1.__color)
print(c1.get_color())

# NO!!!
# c1.brand = "bmw"
# c1.year = 2018
# NO!!!
print(c1.get_brand())