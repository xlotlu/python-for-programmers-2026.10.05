# 1. creați un string fromat din string-ul "tralala"
# concatenat cu sine de 7 ori.

print("tralala" * 7)


# 2. obțineți partea întreagă a împărțirii lui 17 la 4
# print(int(17 / 4))
print(17 // 4)


# 3. obțineți restul împărțirii lui 17 la 4
print(17 % 4)


# 4. scrieți o funcție `cube(x)` ce returnează
# pe x ridicat la puterea a 3a.
def cube(x):
    return x ** 3


# 5. cereți utilizatorului să introducă un număr întreg.
# folosiți funcția `input_int()` scrisă ieri.
# După obținerea numărului folosiți `cube()` de mai sus
# pentru a scrie utilizatorului:
# "Cubul numărului <număr> este <rezultat>."
def input_int(prompt=""):
    while True:
        number = input(prompt)
        # vedem dacă stringul e număr întreg valid

        if number.isdecimal():
            return int(number)

        print("Număr invalid!")

num = input_int("Spune-mi un număr: ")
print(f"Cubul numărului {num} este {cube(num)}.")


# 6. printați numerele de la 100 la 125 folosind while.
x = 100
while x <= 125:
    print(x)
    x += 1


# 7. scrieți o funcție
def format_minutes(total_minutes):
    pass
# ce primind un număr întreg
# returnează un string formatat "ore:minute".
# exemplu: format_minutes(62) -> "1:02".
#
# pentru a obține un string cu padding de zero-uri
# de forma "02", aveți variantele:
# a) dacă vreți să gândiți algoritmul,
#    folosiți funcția `len(string)`, sau
# b) inspectați metodele str și vedeți ce vă poate ajuta,
#    fără să consultați google. :)

def format_minutes(mins):
    hours = mins // 60
    minutes = mins % 60

    if minutes < 10:
        # pad-uim cu zero
        pass

    if len(str(minutes)) == 1:
        # pad-uim cu zero
        pass

    # sau
    str(minutes).rjust(2, "0")

    # sau
    return f"{hours}:{minutes:02d}"

# max compactness:
def format_minutes(total_minutes):
    hours, minutes = divmod(total_minutes, 60)
    return f"{hours}:{minutes:02d}"


# 8. [opțional] scrieți o funcție
def get_seconds_from_now(timespec):
    pass
# ce returnează numărul de secunde din momentul curent
# pănă la următoarea apariție a lui `timespec`.
#
# considerați `timespec` în format "HH:MM".
# puteți folosi brute-force parsing (str.split(':'))
# sau datetime.time.strptime
#
# sosul secret se găsește în modulul `datetime`,
# în clasele `datetime` și `time`.
#
# puteți folosi google, nu A.I.



import datetime as dt

def get_seconds_from_now(timespec):
    #hour, minute = timespec.split(':')
    time = dt.time.strptime(timespec, '%H:%M')
    now = dt.datetime.now()

    then = now.replace(hour=time.hour, minute=time.minute, second=0)

    # if "then" is in the past,
    # then we need to look for tomorrow
    if then < now:
        then += dt.timedelta(days=1)

    diff = then - now

    return diff.total_seconds()

# TODO:
# (temă pentru acasă)
# faceți funcția `get_seconds_from_now()`
# să suporte timespec de forma
# "HH:MM" și "HH:MM:SS"
#
# poate folosim dt.time.fromisoformat() ?
