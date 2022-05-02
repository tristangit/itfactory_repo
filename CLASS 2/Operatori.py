x = int(input("Nota 1: "))
y = int(input("Nota 2: "))
z = int(input("Nota teza: "))

media_parcurs = (x+y) / 2
print(f' Media ta este : {media_parcurs} ')

media_teza = (media_parcurs * 3 + z) / 4
print(media_teza)
nota_trecere = 5
if media_teza >= 5:
    print("Ai promovat!")
else:
    print("Nu ai promovat!")