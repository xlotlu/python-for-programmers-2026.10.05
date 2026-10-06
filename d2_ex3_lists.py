lst = ["ala", "bala", "porto", "cala"]

# adăugăm UN element:
lst.append["un singur element"]

# adăugăm MAI MULTE elemente:
lst.extend[["încă ceva", "și încă ceva"]]

# poate fi extins cu elementele din ORICE iterabil
lst.extend[range[5]]

# inserăm un element nou la o poziție dată:
lst.insert[1, "trala"]


# scoatem și returnăm ultimul element din listă:
lst.pop()

# scoatem și returnăm primul element din listă:
lst.pop(0)


# .pop() este echivalent cu:
def pop(lst, idx):
    v = lst[idx]
    del lst[idx]
    return v


# atenție la funcțiile care mutează lista
# fără să țină cont de ce se întâmpla în afara
# funcției
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

def augment_cities(cities):
    for elem in cities:
        ceva_nou = random.randint(50, 80)
        elem.append(ceva_nou)
    return cities

print(augment_cities(cities))
print(cities)
print("\N{FACE SCREAMING IN FEAR}")

# în astfel de cazuri, probabil e o idee bună
# să ne creăm o listă nouă în interiorul funcției
def augment_cities(cities):
    cities = cities.copy()

    for elem in cities:
        ceva_nou = random.randint(50, 80)
        elem.append(ceva_nou)

    return cities


# ștergerea unui element din listă:
lst = ["ala", "bala", "ala", "porto", "cala", "ala"]
lst.remove("ala")

# echivalent cu:
# a găsi indexul elementului
idx = lst.index("ala")
# și apoi a șterge (de la) indexul respectiv
del lst[idx]


# cu sintaxa de item access se poat face modificări in-place:
lst[2] = "o altă valoare"


# numărăm apariția unui element:
lst.count("ala")

# Task:
# sortați case-insensitive următoarea listă:

l = [
    "Aaa",
    "ABa",
    "AAb",
]

"aaa", "aab", "aba"

# l.sort() rezultă în:
['AAb', 'ABa', 'Aaa']
# nu este ce vrem!

# soluția: creăm o funcție cheie de sortare
def normalize(elem):
    return elem.lower()

l.sort(key=normalize)

# introducem lambda:
something = lambda num: 'WOW!' * num
# echivalent cu:
def something(num):
    return 'WOW!' * num

# exemplul de mai sus cu lambda:
l.sort(key=lambda elem: elem.lower())


# Exercițiu:
# Dată fiind lista cu nume și distanțe ale orașelor
# de mai sus, ordonați lista după distanță
cities.sort(key=lambda c: c[1])



# Exercițiu:
# citiți documentația funcției `filter()`
# și repetați exercițiul de filtrare
# a orașelor după distanță folosindu-l pe filter()

def filterer(elem):
    return elem[1] < 200

for elem in filter(filterer, cities):
    print(elem)

# și cu lambda:
print(list(
    filter(lambda elem: elem[1] < 200, cities)
))


# Task:
# creați o listă nouă cu orașele cu distanță < 300,
# iterând prin lista originală de orașe cu distanțele lor
# astfel încât în timpul iterației să consumați lista inițială.
#
# (deci la sfârșitul iterației cities va fi gol)

filtered_cities = []

while cities:
    elem = cities.pop() # aceasta este operație O(1) --> O(n)

    if elem[1] < 300:
        filtered_cities.append(elem)

# întrebare: cum păstrăm ordinea inițială?
# răspuns:
filtered_cities.reverse()  # aceasta este operație O(n)

# sau:
filtered_cities = []

while cities:
    # aceasta implică re-indexare totală
    elem = cities.pop(0) # aceasta este operație O(n^2)

    if elem[1] < 300:
        filtered_cities.append(elem)

# operațiuni care implică re-indexarea listei:
# .pop(idx)
# del lst[idx]
# .remove()
# .index()
# ( și .sort() și .reverse() )

# pentru situațiile când sunt necesare
# operațiuni multiple de inserție / pop
# pe seturi mari de date:

from collections import deque

# deque = chained list
#         implicație:   orice inserție sau pop-uire
#                       nu duce la reindexare
#         implicația 2: accesul după index nu este optimizat
#
# list  = contiguous
#         implicație:   orice inserție sau pop-uire
#                       altfel decât la sfârșit
#                       înseamnă reindexare
#         implicația 2: accesul după index este hiper-optimizat
