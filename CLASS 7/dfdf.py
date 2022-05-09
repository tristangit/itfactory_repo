class FormaGeometrica(ABC):


    @public
    Pi = 3.14 # aici nu inteleg cum sa il folosesc pe Pi in clasa Cerc(FormaGeometrica)
    pi = 3.14 # aici nu inteleg cum sa il folosesc pe Pi in clasa Cerc(FormaGeometrica)


    @abstractmethod
@@ -52,7 +51,7 @@ def get_raza(self):


    def aria(self):
        return Pi * self.__raza ** 2
        return self.pi * self.__raza ** 2


    def set_raza(self, alta_valoare):
@@ -69,29 +68,27 @@ def descrie(self):
l1 = Patrat(5)
R1 = Cerc(2)

# print(l1.get_latura())
#
# l1.set_latura(4)
# print(l1.get_latura())
# l1.del_latura()
# try:
#     print(l1.get_latura())
# except Exception as e:
#     print(e)
#
# print(R1.get_raza())
# R1.set_raza(4)
# print(R1.get_raza())
#
# R1.del_raza()
#
# try:
#     print(R1.get_raza())
# except Exception as e:
#     print(e)
# print(R1.descrie())

print(l1.aria()) # aici cred ca nu trebuie sa introduc eu manual argumentul, nu am stiut cum sa
                         # il ia automat din declarerea variabile
print(R1.aria())   # aici cred ca nu trebuie sa introduc eu manual argumentul, nu am stiut cum sa
                         # il ia automat din declarerea variabile
print(l1.aria())
print(R1.aria())

print(l1.get_latura())

l1.set_latura(4)
print(l1.get_latura())
l1.del_latura()
try:
    print(l1.get_latura())
except Exception as e:
    print(e)

print(R1.get_raza())
R1.set_raza(4)
print(R1.get_raza())

R1.del_raza()

try:
    print(R1.get_raza())
except Exception as e:
    print(e)
print(R1.descrie())