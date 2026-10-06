fp = open("demo.txt")

# Modalitatea #1 de a citi content dintr-un fișier:
#
# dacă vrem tot content-ul deodată
# (spre exemplu citim un template dintr-un fișier)
# (sau alte situații în care conținutul nu este line-oriented)
# facem:
fp.read()

# Modalitatea #2: iterăm în fișier:
for line in fp:
    print(line)

# Exercițiu:
# scrieți o funcție
def get_content(path):
    pass
# ce returnează conținutul fișierului de la locația `path`

def get_content(path):
    fp = open(path)
    return fp.read()

# cum lucrăm cu căi pe windows?
# ori facem escape-ing la backslash:
myfile = "C:\\Users\\myuser\\etc\\file.txt"
# ori facem "raw string":
myfile = r"C:\Users\myuser\etc\file.txt"



def emulate_file_access():
    fp = open("demo.txt")
    # operațiuni pe fișier

    1 / 0

    print("închid file pointer-ul")
    fp.close()

# the old way to avoid dangling file pointers:
def emulate_file_access():
    fp = open("demo.txt")

    try:
        # operațiuni pe fișier

        1 / 0
    finally:
        # aici se execută întotdeauna
        # chiar dacă a fost o excepție
        print("închid file pointer-ul")
        fp.close()


# statement nou:
# context manager
def emulate_file_access():
    with open("demo.txt") as fp:
        # operațiuni pe fișier
        1 / 0

"""
# pseudo-exemplu de context manager-ul
# sqlite care face auto-commit / auto-rollback:

# înainte (pe vremuri):
try:
    con.execute("insert whatever")
except SqliteError:
    con.rollback()
else:
    con.commit()

# după inventarea context-manager-elor:
with con:
    con.execute("insert whatever")
"""

# Exercițiu
# Scrieți o funcție
def write_content(path, content):
    pass
# ce scrie str-ul `content` în fișierul `path`.
# nu uitați să folosiți `with` statement

def write_content(path, content):
    with open(path, 'w') as fp:
        fp.write(content)

# luați content-ul
data = """
Salutare,
Eu sunt un string aparent ca oricare string
Doar că am o supriză.

Care este aceea? Și de ce?
"""

# și, folosind funcția `write_content()`
# scrieți-l într-un fișier.

# Problema pe windows va fi excepție:
# UnicodeEncodeError: 'charmap' codec can't encode character '\u0103' in position 64

# anume, încearcă să scrie caracterul "ă" folosind econding default al windows-ului (cp1252)
# care nu cunoaște așa ceva

# Fix-ul?
# specificăm întotdeauna(!) encoding-ul,
# care (în 99.9% cazuri) vreți să fie "utf-8".

# reparăm funcțiile de mai sus:

def read_content(path, encoding="utf-8"):
    with open(path, encoding=encoding) as fp:
        return fp.read()

def write_content(path, content, encoding="utf-8"):
    with open(path, 'w', encoding=encoding) as fp:
        fp.write(content)
