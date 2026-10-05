x = 2
y = 2

# toate statement-urile care suportă sub-bloc
# se termină cu ':'
# iar sub-blocul este indentat
#                     la același nivel

if x == y:
    print("they are equal")
    print("so all is fine!")

### echivalent cu:
# if (x == y) {
#     print("they are equal");
#     print("so all is fine!");
# }

""" # tocmai am abuzat string-ul drept comentariu
# full syntax:
if condition_1:
    statements_1
elif condition_2:
    statements_2
# ....
elif condition_n:
    statements_n
else:
    final_statement

# partial syntax #1
if condition:
    statement

# partial syntax #2
if condition:
    statement
else:
    alt_statement

# partial syntax #3
if condition_1:
    statements_1
elif condition_2:
    statements_2
"""

# Exercițiu:
# Cereți vârsta utilizatorului cu input()
# - dacă este mai tânăr de 18 ani
#   anunțați-l că este prea tânăr;
# - altfel anunțați-l că este acceptat.


MIN_AGE = 18 # soft convention,
             # uppercase var name
             # means it is a "constant"

age = int(input("Introduceti varsta: "))

if age < MIN_AGE:
    print("Prea tanar, mai asteapta", MIN_AGE - age, "ani")
else:
    print("Acceptat")


# Exercițiu:
# Scrieți condiționalele necesare astfel încât
# dată o variabilă

hour = 15 # testați codul cu mai multe valori

# să printeze:
# "Bună dimineața" pentru ore între 5 și 12
# "Bună ziua"      pentru ore între 12 și 18
# "Bună seara"     pentru ore între 18 și 22
# "Noapte bună"    pentru ore între 22 și 5

# avem grijă ca intervalele să fie:
# [A, B)

if hour >= 5 and hour < 12:
    print("Buna dimineata")
elif hour >= 12 and hour < 18:
    print("Buna ziua")
elif hour >= 18 and hour < 22:
    print("Buna seara")
else:
    print("Noapte buna")

# v2: chaining operators:

if 5 <= hour < 12:
    print("Buna dimineata")
elif 12 <= hour < 18:
    print("Buna ziua")
elif 18 <= hour < 22:
    print("Buna seara")
else:
    print("Noapte buna")


# operatori boolean:
"""
==
!=

<
>
<=
>=

not
and
or

in
not in

is
is not
"""