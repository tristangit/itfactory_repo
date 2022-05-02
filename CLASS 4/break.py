



#vrem sa verificam ca o lista are numai elemente numerice

l1 = [15, 22, 'Ana', 3588, -88]
l2 = [156546, 65456, 89, 4]

n1 = len(l1)
n2 = len(l2)

# #verificam prima lista
# for i in range(n1):
#     if not (type(l1[i]) is int):
#         print(f'Lista l1 nu este numerica')
#         break
#     print(f' {l1[i]} a fost evaluata')
#     # else:
#     #     print(f'Lista l1 este numerica')

found_nonnumerical_element = False
#verificam prima lista
for i in range(n1):
    if not (type(l1[i]) is int):
        found_nonnumerical_element = True
        # print(f'Lista l1 nu este numerica')
        break
    # print(f' {l1[i]} a fost evaluata')
    # else:
    #     print(f'Lista l1 este numerica')

if found_nonnumerical_element == True:
    print(f'Nu, lista l1 nu este numerica')
else:
    print(f'DA, este numerica ')
