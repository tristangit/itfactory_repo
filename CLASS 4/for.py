# x = ['Ana', 'monom', '101', 'cartof', '543', 'bob']
# l = len(x)
# i = 0
# for i in range(l):
#     s = x[i].lower()
#     if s[::-1] == s:
#         print(f'Sirul {s} este un palindrom')
#     else:
#         print(f'Sirul {s} nu este un palindrom')






# while i < l:
#     s = x[i].lower()
#     if s[::-1] == s:
#         print(f'Sirul {s} este un palindrom')
#     else:
#         print(f'Sirul {s} nu este un palindrom')
#     i += 1
# else:
#     print(f'Bucla while s-a terminat')


x = [1, 'Ana', 'monom', 101, 'cartof', 543, 'bob']
l = len(x)
i = 0
for i in range(l):
    if str(x[i]).isnumeric():
        print(f'Elementul {x[i]} este numeric')
    else:
        print(f'Elementul {x[i]} nu este numeric')

