numar1 = int(input("Primul numar introdus este: "))
numar2 = int(input("Al 2 lea numar introdus este: "))
operator = input("Operatorul este: ")

if operator == "+":
    print(numar1 + numar2)
elif operator == "-":
    print(numar1 - numar2)
elif operator == "*":
    print(numar1 * numar2)
elif operator == "/":
    if numar2 == 0:
        print("Nu se poate realiza impartirea cu 0")
    else:
        print(numar1 / numar2)
elif operator == "%":
    print(numar1%numar2)
elif operator == "**":
    print(numar1**numar2)
else:
    print("Introdu un operator aritmetic")