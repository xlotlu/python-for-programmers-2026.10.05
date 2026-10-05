#while condition:
#    statement

# Exercițiu
# Atâta timp cât utilizatorul
# declară că are vârsta mai mică decât 18 ani,
# este anunțat că nu este acceptat,
# și se cere din nou vârsta.

# 1. cerem vârsta
varsta = int(input("Varsta este: "))

# 2. intrăm în buclă
while varsta < 18:
    print("Ești prea tânăr, next?")
    varsta = int(input("Varsta este: "))

print(f"ok, tu ai {varsta} ani.")


# v. alternativă, buclă infinită:
while True:
    varsta = int(input("Varsta este: "))
    # dar acum trebuie să scăpăm explicit

    if varsta < 18:
        print("Ești prea tânăr, next?")
    else:
        print(f"ok, tu ai {varsta} ani.")
        break

# control flow statements when looping:
# (i.e. inside `for` and `while`)
# break
# continue

# v. alternativ-alternativă, buclă infinită,
# cu continue și break
while True:
    varsta = int(input("Varsta este: "))
    # dar acum trebuie să scăpăm explicit

    if varsta < 18:
        print("Ești prea tânăr, next?")
        continue

    print(f"ok, tu ai {varsta} ani.")
    break

# Exercițiu:
# Scrieți o funcție
def input_int(prompt=""):
    pass
# ce promptează utilizatorul
# (cu promptul opțional `prompt`)
# și returnează în momentul în care
# a primit un număr întreg valid
#
# sau, altfel, dă mesaj de eroare
# și continuă să ceară un număr întreg.



# în momentul în care vă dați seama
# că vă lipsește sosul secret
# vă rog, vorbiți


def input_int(prompt=""):
    while True:
        number = int(input(prompt)) # <-- avem nevoie de o protecție
        return number

# varianta 1:
# - cerem input
# - vedem dacă stringul e număr întreg valid
# - dacă da, returnăm; dacă nu, buclăm.

def input_int(prompt=""):
    while True:
        number = input(prompt)
        # vedem dacă stringul e număr întreg valid

        if number.isdecimal():
            return int(number)

        print("Număr invalid!")


# varianta 2:
# - cerem input
# - facem direct int() pe el
# - dacă avem eroare o capturăm(!) și buclăm
# - altfel returnăm

def input_int(prompt=""):
    while True:
        number = input(prompt)

        try:
            number = int(number)
        except ValueError:
            print("Număr invalid!")
        else:
            return number

