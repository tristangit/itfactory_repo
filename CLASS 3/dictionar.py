
d = {
    "prenume" : "Ion",
    "nume" : "Popescu",
    "varsta" : 25,
    "localitate" : "Brasov"
    "permise" : ['b', 'c', 'd']
}

print(f'Dictionarul are {len(d)} elemente')
print(f"Numele complet este: {d['prenume']} {d['nume']} ")
print(f"Varsta lui este de {d['varsta']} ani ")

d['profesie'] = 'informatician'
print(f'Dictionarul are {len(d)} elemente')
print(d)