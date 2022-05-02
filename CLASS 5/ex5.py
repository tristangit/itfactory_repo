def pitagora(c1, c2, ip):
    if ip**2 == c1**2 + c2**2:
#        print("Triunghiul este unul dreptunghic")
        return True
    else:
#        print("Triunghiul nu este dreptunghic")
        return False


cat1 = int(input("Introduceti valoarea primei catete: "))
cat2 = int(input("Introduceti valoarea celei de a 2 a catete: "))
ip = int(input("Introduceti valoarea ipotenuzei: "))
rez = pitagora(cat1, cat2, ip)
if rez == True:
    print("Triunghiul este unul dreptunghic")
else:
    print("Triunghiul nu este dreptunghic")