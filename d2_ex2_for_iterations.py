#for elem in iterable:
#    do_something_with(elem)

# "sequence" types:

lst = ["ala", "bala", "porto", "cala"]
tup = ("ala", "bala", "porto", "cala")
s = "Bună dimineața!"

for elem in lst:
    print(elem)
for elem in tup:
    print(elem)
for elem in s:
    # str este iterabil char by char
    print(elem)


lst[0] # item access
s[0]

lst[-1]
s[-1]

# range-ul este un obiect iterabil
for elem in range(100, 120):
    print(elem)



from itertools import cycle

# dovadă că iterabilele pot fi "infinite"
# (plus învățat despre zip)
# (și multiple variable assignment ("unpacking")
#  în mijlocul for-ului)
for value, cls in zip(lst, cycle(["odd", "even"])):
    print(f'<tr class="{cls}"><td>{value}</td></tr>')


# Exercițiu:
# dată fiind lista de orașe
cities = [
 'Cluj-Napoca',
 'Timișoara',
 'Iași',
 'Constanța',
 'Brașov',
 'Craiova',
 'Galați',
 'Ploiești',
 'Oradea',
 'Sibiu',
 'Arad',
 'Bacău',
 'Brăila',
 'Buzău',
 'Suceava',
 'Pitești',
 'Târgu Mureș',
 'Baia Mare',
]

# iterați în listă
# și printați elementele care încep cu litera "B"
for c in cities:
    if c[0] == "B":
        print(c)

# sau
for c in cities:
    if c.startswith("B"):
        print(c)


# Exercițiu:
# dată fiind lista de tuple de forma
# (oraș, distanță)
cities = [
    ('Cluj-Napoca', 450),
    ('Timișoara', 550),
    ('Iași', 390),
    ('Constanța', 225),
    ('Brașov', 180),
    ('Craiova', 230),
    ('Galați', 250),
    ('Ploiești', 60),
    ('Oradea', 610),
    ('Sibiu', 275),
    ('Arad', 560),
    ('Bacău', 300),
    ('Brăila', 200),
    ('Buzău', 110),
    ('Suceava', 450),
    ('Pitești', 120),
    ('Târgu Mureș', 330),
    ('Baia Mare', 600),
]

# printați orașele cu distanță mai mică decât 300
for tup in cities:
    if tup[1] < 300:
        print(tup[0])

# sau
for city, distance in cities:
    if distance < 300:
        print(city)


# Exercițiu:
# știind că lista are metoda `.append()`
# scrieți o funcție
def filter_cities(cities, distance):
    pass
# ce returnează o listă nouă
# cu tuplele (oraș, distanță)
# ce au distanța mai mică decât `distance`.

# pattern de acumulare
def filter_cities(cities, distance):
    # 1. ne definim obiectul în care acumulăm
    out = []

    # 2. iterăm în datele-sursă
    for tup in cities:
        # 3. filtrăm
        if tup[1] < distance:
            # 4. acumulăm
            out.append(tup)

    # 5. returnăm
    return out
