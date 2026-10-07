# dicționarul:
{ "cheie": "valoare", "cheie 2": "valoare 2" }

d = { "cheie": "valoare", "cheie 2": "valoare 2" }

# clasa sursă:
dict

# instanțiere de dicționar gol:
dict()

# echivalent cu:
{}

# dicționarul gol este false-y:
bool( dict() )


d = { "cheie": "valoare", "cheie 2": "valoare 2" }

# item access
d["cheie"]

# assignment
d["cheie"] = "valoare nouă"

# creare de cheie nouă, aceeași sintaxă:
d["cheie nouă"] = "altceva"

# scoatem o cheie din dicționar și îi obținem valoarea
d.pop("cheie")

# scoatem o pereche (key, value):
d.popitem()

# alte metode:
d.clear()
d.copy()

# când vrem să obținem întotdeauna o valoare
# chiar dacă cheia nu există, folosim d.get():

d.get("my key")
val = d.get("my key", "my default value")

# echivalent cu:
try:
    val = d["my key"]
except KeyError:
    val = "my default value"

# inversul lui get, setăm o valoare
# doar dacă nu există:
d.setdefault("cheie", "my default value")
d.setdefault("my new key", "my default value")

# merge-uim un alt dicționar în acesta existent:
d.update({
  "cheie": "ALTCEVA",
  "și altă cheie": "încă ceva",
  })

# metodele de iterare:
d.values()
d.keys()
d.items()

for elem in d.items():
    print(elem)

# uzual:
for k, v in d.items():
    print(k, v, sep="» ")

# și la final:
dict.fromkeys # "class method"
dict.fromkeys(["k1", "k2", "k3"])
dict.fromkeys(["k1", "k2", "k3"], "valoare")


# Exercițiu:
# dată fiind lista de liste
cities = [
    ['Cluj-Napoca', 450],
    ['Timișoara', 550],
    ['Iași', 390],
    ['Constanța', 225],
    ['Brașov', 180],
    ['Craiova', 230],
    ['Galați', 250],
    ['Ploiești', 60],
    ['Oradea', 610],
    ['Sibiu', 275],
    ['Arad', 560],
    ['Bacău', 300],
    ['Brăila', 200],
    ['Buzău', 110],
    ['Suceava', 450],
    ['Pitești', 120],
    ['Târgu Mureș', 330],
    ['Baia Mare', 600],
]
# creați un dicționar nou
# cu chei numele orașelor, respectiv
# valori distanța

d_cities = {}
for c in cities:
    d_cities[c[0]] = c[1]
# prettier
for name, dist in cities:
    d_cities[name] = dist

# dată fiind o structură iterabilă
# ale cărei elemente sunt la rândul lor
# iterabile cu două elemente (!),
#
# un dicționar poate fi instanțiat din aceasta
iter = (
  ("k", "v"),
  ("x", "y"),
)
dict(iter)

# deci...
d_cities = dict(cities)

# use case:
# avem 2 seturi de date columnare
# care au corespondență 1 la 1:
names = [
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
]

distances = [
    450, 550, 390,
    225, 180, 230,
    250, 60, 610,
    275,
]

# cum putem genera rapid, simplu, progragramatic
# un dicționar name: distance?

# idee: acces după index:
for idx in range(len(names)):
    name = names[idx]
    dist = distances[idx]

    # acum putem popula dicționarul

# sau, unim seturile de date cu `zip()`
# și instanțiem dicționarul direct:
dict(zip(names, distances))

# cerință:
# dată fiind lista de liste `cities`
# creați o listă nouă ce conține dicționare
# de forma {"name": <numele>, "distance": <distanța>}


cities_dict_list = []

for name, distance in cities:
    cities_dict_list.append({
        "name": name,
        "distance": distance,
    })

print(cities_dict_list)

# dat fiind dataset-ul cities augmentat cu 
# coloanele noi "population" și "altitude"
cities_augm = [
 ['Cluj-Napoca', 450, 197000, 715],
 ['Timișoara', 550, 197000, 161],
 ['Iași', 390, 142000, 326],
 ['Constanța', 225, 120000, 795],
 ['Brașov', 180, 128000, 757],
 ['Craiova', 230, 136000, 439],
 ['Galați', 250, 163000, 295],
 ['Ploiești', 60, 193000, 186],
 ['Oradea', 610, 191000, 476],
 ['Sibiu', 275, 163000, 1014],
 ['Arad', 560, 150000, 1173],
 ['Bacău', 300, 186000, 141],
 ['Brăila', 200, 150000, 169],
 ['Buzău', 110, 196000, 475],
 ['Suceava', 450, 151000, 814],
 ['Pitești', 120, 121000, 977],
 ['Târgu Mureș', 330, 157000, 1133],
 ['Baia Mare', 600, 182000, 1083]
]
# repetați exercițiul de mai sus
cities_dict_list = []

for elem in cities_augm:
    cities_dict_list.append({
        "name": elem[0],
        "distance": elem[1],
        "population": elem[2],
        "altitude": elem[3],
    })

print(cities_dict_list)

# găsim o metodă mai elegantă decât să rescriem codul
# de fiecare dată când apare o coloană nouă?

# să știm "undeva" care sunt cheile
# în loc să le scriem de mână, automatizăm cumva
columns = ["name", "distance", "population", "altitude"]

cities_dict_list = []
for elem in cities_augm:
    city = {}
    for idx in range(len(columns)):
        k = columns[idx]
        v = elem[idx]

        city[k] = v

    cities_dict_list.append(city)

# fix același lucru dar mai pythonic,
# cu enumerate() în loc de range(len()):

columns = ["name", "distance", "population", "altitude"]

cities_dict_list = []
for elem in cities_augm:
    city = {}
    for idx, k in enumerate(columns):
        v = elem[idx]

        city[k] = v

    cities_dict_list.append(city)

# sau, folosim zip():
columns = ["name", "distance", "population", "altitude"]

cities_dict_list = []
for elem in cities_augm:
    cities_dict_list.append(
        dict(zip(columns, elem))
    )

# ======= #

# introducem comprehensions
# cerință: dată fiind lista
l = [1, 2, 5, 7]
# creați o listă nouă cu pătratele nr.-lor

lsq = []
for elem in l:
    lsq.append(elem ** 2)

# cu _list comprehension_:
[    elem ** 2    for elem in l    ]

# cerință: dată fiind lista
l = [1, 2, 3, 4, 5, 6, 7]
# creați o listă nouă cu pătratele
# numerelor impare
lsqimp = []
for elem in l:
    if elem % 2:
        lsqimp.append(elem ** 2)

[  elem ** 2    for elem in l    if elem % 2    ]
# prettyfication for readability:
[
    elem ** 2
    for elem in l
    if elem % 2
]

# poate fi multi-level:
mx = [ [1, 2], [3, 4], [5, 6] ]
[ cell for row in mx for cell in row ]
# echivalent cu:
result = []
for row in mx:
    for cell in row:
        result.append(cell)

# și acum _dict comprehension_:
cities = [
 ['Cluj-Napoca', 450],
 ['Timișoara', 550],
 ['Iași', 390],
 ['Constanța', 225],
 ['Brașov', 180],
]

d_cities = {}
for name, dist in cities:
    d_cities[name] = dist

{
    name: dist
    for name, dist in cities
}

# să refacem acest exercițiu:
columns = ["name", "distance", "population", "altitude"]

cities_dict_list = []
for elem in cities_augm:
    cities_dict_list.append(
        dict(zip(columns, elem))
    )
# transformați-l în list comprehension
[
    dict(zip(columns,elem))
    for elem in cities_augm
]



# dată fiind structura de date
# formată dintr-o listă de [name, age, hobbies]
friends = {
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
}

# și funcția

def get_by_name(friends, name):
    for friend in friends:
        if name == friend[0]:
            return friend


# Q: Putem să optimizăm cumva look-up-ul de get_by_name()
# astfel încât să nu se facă search în tot dataset-ul la fiecare retrieval?

# A: Putem dacă folosim un dicționar. # unde și cum am crea acest dicționar?!?

_friends_dict_cache = {
    # dicționar cu cheie numele
    friend[0]: friend
    for friend in friends
}

def get_by_name(friends, name):
    return _friends_dict_cache[name]

# haidem să ascundem acest cache să nu poluăm global namespace
# strategie: îl agățăm de funcție
#            drept atribut al funcției

# "memoization"
def get_by_name(friends, name):
    # verific dacă există cache-ul
    try:
        cache = get_by_name._friends_dict_cache
    except AttributeError:
        # dacă nu există îl creez
        cache = get_by_name._friends_dict_cache = {
            friend[0]: friend
            for friend in friends
        }
        print("am creat cache")
    else:
        # dacă exista cache-ul
        # verificăm dacă este proaspăt
        if len(cache) != len(friends):
            # TODO: refresh cache
            pass

    """
    # atenție, asta va genera KeyError
    return cache[name]
    # old behaviour era return None

    # ce variante avem să nu dăm KeyError?
    try:
        return cache[name]
    except KeyError:
        return
    """

    return cache.get(name)
