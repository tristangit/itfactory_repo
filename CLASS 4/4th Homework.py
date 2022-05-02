# # 1.
# # Avand lista
# # masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# #
# # Folositi un for ca sa iterati prin toata lista si sa afisati
# # ‘Masina mea preferata este x’
# # Faceti acelasi lucru cu un for each
# # Faceti acelasi lucru cu un while
#
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in masini:
#     print(f'Masina mea preferata este {i}')
#
# print()
#
# lenght = len(masini)
# for i in range(lenght):
#     print(masini[i])
# print()
# print('================================================')
# #while
# lenght = len(masini)
# i = 0
# while i < lenght:
#     print(masini[i])
#     i+=1
# print('================================================')
# print('================================================')
# print('================================================')
#
#
#
# # 2.
# # Aceeasi lista
# # Folositi un for else
# # In for
# #    Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# # In else
# #    Printati lista

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# a = len(masini)
# #b = masini[1:][:-1]
#
#
# for i in masini[1:-1:1]:
#     print(i.upper())
# else:
#     print(masini)

# 3.
# Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin modalitatea aleasa de voi
# Daca masina e mercedes
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# a = len(masini)
#
# for i in range(a):
#     print(masini[i])
#     if masini[i] == 'Mercedes':
#         print('Am gasit masina dorita de dvs')
#         break
# else:
#     print(f'Am gasit masina {i}. Mai cautam')


#
# 4.
# Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun
# Iterati prin lista
#
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# (nu trebuie else)
# Printati S-ar putea sa va placa masina x

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
a = len(masini)