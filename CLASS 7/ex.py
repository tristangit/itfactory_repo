# x = int(input("x="))
# y = int(input("y="))
#
# z = x / y
# print(f'z = x / y = {z}')

print('First Hello World')

try:
    l = ['abc', 5, 100]
    print(l[5])
except Exception as ex:
    print("---A avut loc o exceptie---")
    print(f'Detaliile exceptiei: {ex} ')
    
