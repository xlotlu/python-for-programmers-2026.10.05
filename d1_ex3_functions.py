"""
def myfunc():
    statement
    statement
    etc

    while something:
        statement
        statement
        etc

        for var in collection:
            statement
            statement
            etc
"""

# Exercițiu:
# Scrieți o funcție
def get_greeting(hour):
    pass
# ce returnează:
# "Bună dimineața" pentru ore între 5 și 12
# "Bună ziua"      pentru ore între 12 și 18
# "Bună seara"     pentru ore între 18 și 22
# "Noapte bună"    pentru ore între 22 și 5


# funcțiile se scriu (de obicei!) cu snake_case

def get_greeting(hour):
    if hour < 0 or hour >= 24:
        raise ValueError("Ora introdusa nu este valida!")

    if 5 <= hour < 12:
        return "Buna dimineata"
    elif 12 <= hour < 18:
        return "Buna ziua"
    elif 18 <= hour < 21:
        return "Buna seara"
    elif 21 <= hour < 24 or 0 <= hour < 5:
        return "Noapte buna"


for h in (
        1, 4, 5, 6, # boundary values
        11, 12, 13, # very good idea when testing
        17, 18, 19,
        22,
        24
    ):

    print(h, get_greeting(h), sep=" :: ")


#print(get_greeting("z4"))

# Exercițiu:
# Scrieți o funcție
def get_current_greeting():
    pass
# ce returnează salutul potrivit
# pentru momentul curent al zilei
#
# refolosiți funcția get_greeting()
# fără a îi modifica codul.

from datetime import datetime

def get_current_greeting():
    now = datetime.now()
    return get_greeting(now.hour)


# Exercițiu
# Scrieți o funcție
def greet_user():
    pass
# ce cere numele utilizatorului
# și îl salută conform cu momentul curent
# (exemplu: "Bună ziua, Gigel")

def greet_user():
    name = input("Numele tău » ")
    greeting = get_current_greeting()

    print(f"{greeting} {name}!")