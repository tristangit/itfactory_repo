z = 0

try:
    x = int(input("x="))
    y = int(input("y="))
    z = x / y
except Exception as ex:
    print(f'A avut loc o exceptie')
    print(f'Detalii despre exceptie: {ex}')

print(f'z = x / y = {z}')