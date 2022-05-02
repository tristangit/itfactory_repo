d = {
    "prenume" : "Ion",
    "nume" : "Popescu",
    "varsta" : 25,
    "localitate" : "Brasov",
    "permise_auto" : ['b', 'c', 'd']
}

print(f"Dictionarul are {len(d)} elemente!")
print(f"Numele complet este: {d['prenume']} {d['nume']}")
print(d['varsta'])
print(d)

print("======================================")
d['profesie'] = 'informatician'
print(f"Dictionarul are {len(d)} elemente!")
print(d)