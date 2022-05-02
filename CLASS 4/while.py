# i = 0
# while i <= 10:
#     print(i)
#     i += 2


# i = 0
# while i <= 10:
#     if i%2 == 0:
#         print(i)
#     else:
#         # print('Numarul este impar')
#         print(f'Numarul {i} este impar')
#     i += 1

# i = 0
# pare = []
# impare = []
# while i <= 100:
#     print(f'Am ajuns la pasule {i}')
#     if i%2 == 0:
#         pare.append(i)
#         # print(i)
#     else:
#         # print('Numarul este impar')
#         # print(f'Numarul {i} este impar')
#         impare.append(i)
#     i += 1
# print(f'Numerele pare sunt {pare} ')
# print(f'Numerele impare sunt {impare} ')

# x = ['Ana', 'monom', 101, 'cartof', 543, 'bob']
# y = len(x)
# print(y)
# i = 0
# while i < y:
#     print(x[i])
#     i += 1
# else:
#     print(f'Am terminat de parcurs lista')

x = ['Ana', 'monom', '101', 'cartof', '543', 'bob']
l = len(x)
i = 0
while i < l:
    s = x[i].lower()
    if s[::-1] == s:
        print(f'Sirul {s} este un palindrom')
    else:
        print(f'Sirul {s} nu este un palindrom')
    i += 1
else:
    print(f'Bucla while s-a terminat')


