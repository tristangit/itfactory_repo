numar1 = int(input("Primul numar este :"))
numar2 = int(input("Al doilea numar este :"))
operator = input("operator: ")
if operator == "+":
    print(numar1+numar2)
elif operator == "-":
    print(numar1-numar2)
elif operator == "*":
    print(numar1*numar2)
elif operator == "/":
    print(numar1/numar2)
else:
    print("Nu e corect, alege ceva bine")
