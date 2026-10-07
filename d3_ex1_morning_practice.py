# 1. dat fiind string-ul
s = "Bună dimineața, ce soare frumos!"

# a) obțineți substringul de la caracterele 2 la 9
# al 2lea la al 9lea
s[1:9]

# b) obțineți primele 4 caractere
s[:4]

# c) ultimele 5 caractere
s[-5:]

# d) de la indexul 5 la 8 inclusiv
s[5:8+1]

# e) tot string-ul de la coadă la cap
s[::-1]

# 2. scrieți o funcție
def grep(path, match, encoding="utf-8"):
    pass
# ce printează toate liniile din fișierul `path`
# care conțin substring-ul `match`
def grep(path, match, encoding="utf-8"):
    with open(path, encoding=encoding) as f:
        for line in f:
            if match in line:
                print(line.removesuffix("\n"))


# 3. rescrieți funcția grep astfel:
def grep(path, match, insensitive=False, encoding="utf-8"):
    pass
# și faceți-o să returneze o listă cu toate liniile
# care fac match
def grep(path, match, insensitive=False, encoding="utf-8"):
    if insensitive:
        match = match.lower()

    lines = []

    with open(path, encoding=encoding) as f:
        for line in f:
            mline = line.lower() if insensitive else line

            if match in mline:
                lines.append(line.removesuffix("\n"))

    return lines


# 4. scrieți o funcție
def grepinto(infile, outfile, match, encoding="utf-8"):
    pass
# ce scrie în fișierul `outfile` toate liniile din `infile`
# care conțin substring-ul `match`

def grepinto(infile, outfile, match, encoding="utf-8"):
    with open(infile, encoding=encoding) as fin, \
         open(outfile, 'w', encoding=encoding) as fout:
        for line in fin:
            if match in line:
                fout.write(line)


def grepinto(infile, outfile, match, encoding="utf-8"):
    with (
        open(infile, encoding=encoding) as fin,
        open(outfile, 'w', encoding=encoding) as fout,
    ):
        for line in fin:
            if match in line:
                fout.write(line)


# 4bis. scrieți o funcție
def cp(inpath, outpath, overwrite=False):
    pass
# care copiază fișierul `inpath` în `outpath`
# ținând cont de flag-ul `overwrite`

# v.1: merge dar citește totul în memorie
def copy(inpath, outpath, overwrite=False):
    with open(inpath, "rb") as fin, open(outpath, "wb") as fout:
        content = fin.read()
        fout.write(content)

# v.2: buffered reading/writing
def copy(inpath, outpath, overwrite=False, chunk=8192):
    with open(inpath, "rb") as fin, open(outpath, "wb") as fout:
        while True:
            content = fin.read(chunk)
            if not content:
                break
            fout.write(content)

# v.3: același lucru, folosind "walrus operator"
def copy(inpath, outpath, overwrite=False, chunk=8192):
    with open(inpath, "rb") as fin, open(outpath, "wb") as fout:
        while content := fin.read(chunk):
            fout.write(content)


# 5. dată fiind structura de date
# formată dintr-o listă de [name, age, hobbies]
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]

# a) scrieți o funcție
def get_by_name(friends, name):
    pass
# ce returnează elementul din listă cu numele respectiv

def get_by_name(friends, name):
    for friend in friends:
        if name == friend[0]:
            return friend

# b) folosind `get_by_name()` obțineți "row-ul" cu numele "Jane" și
# îmbătrâniți-o pe Jane cu un an
jane = get_by_name(friends, "Jane")
jane[1] += 1

# c) adăugați-i Annei hobby-urile "reading" și "cooking"
anna = get_by_name(friends, "Anna")
anna[2].extend(["reading", "cooking"])

# d) ștergeți-i lui Mike hobby-ul de la indexul 1
mike = get_by_name(friends, "Mike")
del mike[2][1]


print(friends)

# e) adăugați un prieten nou
["Georgie", 22, ["reading", "cooking", "running"]]
friends.append(["Georgie", 22, ["reading", "cooking", "running"]])

# f) scrieți o funcție
def find_by_hobby(friends, hobby):
    pass
# ce returnează un subset al listei inițiale cu prietenii
# cu acel hobby

def find_by_hobby(friends, hobby):
    return [
        f
        for f in friends
        if hobby in f[2]
    ]

# g) scrieți o funcție
def find_by_age(friends, min_age=None, max_age=None):
    pass
# ce returnează un subset al listei inițiale cu prietenii
# cu vârsta cuprinsă între `min_age` și `max_age`


def find_by_age(friends, min_age=None, max_age=None):
    results = []

    for friend in friends:
        if min_age is not None and friend[1] < min_age:
            continue

        if max_age is not None and friend[1] > max_age:
            continue

        results.append(friend)

    return results


def find_by_age(friends, min_age=None, max_age=None):
    return [
        friend
        for friend in friends
        if (
            (min_age is None or friend[1] >= min_age)
            and
            (max_age is None or friend[1] <= max_age)
        )
    ]

# h) chain-uiți funcțiile `find_by_hobby` și `find_by_age`
# pentru a obține lista de prieteni mai în vârstă de 20 de ani
# care sunt pasionați de "hiking"
find_by_hobby(
    find_by_age(friends, min_age=20),
    "hiking"
)

# cireașă pe tort:
# le adăugăm flag-ul buddy = True
for f in find_by_hobby( find_by_age(friends, min_age=20), "hiking"):
    f.append({"buddy": True})
