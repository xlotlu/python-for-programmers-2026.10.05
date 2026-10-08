# 1. dat fiind string-ul
s = """
It was the best of times,
it was the worst of times,
it was the age of wisdom,
it was the age of foolishness,
it was the epoch of belief,
it was the epoch of incredulity,
it was the season of Light,
it was the season of Darkness,
it was the spring of hope,
it was the winter of despair…
"""
# întrebare:
# de câte ori apare fiecare cuvânt unic în `s`?
#
# scrieți o funcție
def count_words(txt, insensitive=True):
    pass
# ce răspunde la această întrebare
# și rulați-o pe `s`.
#
# hint: știm că există str.split()

import re
from collections import defaultdict

def count_words(txt, insensitive=True):
    if insensitive:
        txt = txt.lower()

    # 1. să facem o listă de cuvinte

    ## sanitizare v1:
    # import string
    # for c in string.punctuation + '…':
    #     txt = txt.replace(c, ' ')
    # words = txt.split()

    ## sanitizare v2: regular expressions
    words = re.findall(r'\w+', txt)

    # 2. să numărăm aparițiile unice

    # v1: verificăm noi dacă există
    #     word-ul în dicționar
    result = {}
    for w in words:
        if w not in result:
            result[w] = 0

        result[w] += 1

    # v2: folosim .get()
    result = {}
    for w in words:
        result[w] = result.get(w, 0) + 1

    # v3:
    result = defaultdict(lambda: 0)
    # sau
    result = defaultdict(int)
    for w in words:
        result[w] += 1

    return result



def count_words(txt, insensitive=True):
    if insensitive:
        txt = txt.lower()

    words = re.findall(r'\w+', txt)

    result = defaultdict(int)
    for w in words:
        result[w] += 1

    return result


# 2. dată fiind lista de dicționare
friends = [
 {'name': 'Jane', 'age': 20, 'hobbies': ['reading', 'hiking', 'biking']},
 {'name': 'Mike', 'age': 17, 'hobbies': ['hiking', 'fishing']},
 {'name': 'Anna', 'age': 25, 'hobbies': []},
 {'name': 'Sam', 'age': 40, 'hobbies': ['playing guitar']},
 {'name': 'Dan', 'age': 34, 'hobbies': ['painting', 'reading']},
]
# și dat fiind dicționarul
occupations = {
    "Jane": "nurse",
    "Mike": "firefighter",
    "Anna": "DBA",
    "Sam": "prosecutor",
}
# modificați dicționarele din lista de mai sus
# astfel încât să adăugați cheia "occupation"
# cu valoarea corespondentă.

# v1: iterație via friends
for f in friends:
    # vezi dacă are occupation
    name = f['name']
    try:
        occ = occupations[name]
    except KeyError:
        continue

    f['occupation'] = occ

# v2: iterație via occupations
# mai întâi ne facem un dicționar pt. a optimiza lookup:
_fdict = {
    elem['name']: elem
    for elem in friends
}
for name, occ in occupations.items():
    # fă lookup și adaugă-o ocupație
    f = _fdict[name]
    f['occupation'] = occ

# 3. având o listă de dicționare
people = [
  {'name': 'Jane', 'age': 25},
  {'name': 'John', 'age': 38},
  {'name': 'Andrew', 'age': 19},
  {'name': 'Georgia', 'age': 28},
  {'name': 'Lisa', 'age': 46},
  {'name': 'Carmen', 'age': 68},
  {'name': 'Thomas', 'age': 22},
  {'name': 'Bill', 'age': 31},
  {'name': 'Peter', 'age': 47},
  {'name': 'Stephen', 'age': 42},
]
# scrieți un one-liner ce calculează
# media de vârstă.
#
# folosiți funcția `sum()` ce primește
# ca argument un iterabil
print(
    sum(p['age'] for p in people) / len(people)
)

# 4. folosind aceeași structură de date
# `people` de mai sus,
# calculați într-o singură iterație:
# suma, vârsta minimă, vârsta maximă.
#
# folosiți funcțiile `min()` și `max()`.

ages = [p['age'] for p in people]
sum(ages), min(ages), max(ages)

# dar fără listă intermediară?
import math
total, min_age, max_age = 0, math.inf, 0
for p in people:
    age = p['age']

    total += age
    min_age = min(min_age, age)
    max_age = max(max_age, age)


# 5. refaceți funcția de ieri
def copy(inpath, outpath, overwrite=False, chunk=8192):
    if overwrite is False and os.path.exists(outpath):
        raise FileExistsError("File exists, will not overwrite")

    with open(inpath, "rb") as fin, open(outpath, "wb") as fout:
        while content := fin.read(chunk):
            fout.write(content)
# astfel încât să nu faceți overwrite handling manual,
# ci bazându-vă pe facilitatea funcției `open()`
# de a face overwrite în modul `w` vs. modul `x`.

def copy(inpath, outpath, overwrite=False, chunk=8192):
    mode = "wb" if overwrite else "xb"

    with open(inpath, "rb") as fin, open(outpath, mode) as fout:
        while content := fin.read(chunk):
            fout.write(content)