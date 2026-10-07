# sintaxa completă a funcției

# argumente poziționale:
def myfunc(a, b):
    print("a »", a)
    print("b »", b)

myfunc(1, 2)

# argumente poziționale capturate ("argument packing")
def myfunc(a, b, *args):
    print("a »", a)
    print("b »", b)
    print("args »", args)

myfunc(1, 2, 3, 4, 5)

# adăugăm keyword-arguments
def myfunc(a, b, *args, kw1="default 1", kw2="default 2"):
    print("a »", a)
    print("b »", b)
    print("args »", args)
    print("kw1 »", kw1)
    print("kw2 »", kw2)

myfunc(1, 2, 3, 4, 5, kw1="ceva")

# keyword argument packing
def myfunc(a, b, *args, kw1="default 1", kw2="default 2", **kwargs):
    print("a »", a)
    print("b »", b)
    print("args »", args)
    print("kw1 »", kw1)
    print("kw2 »", kw2)
    print("kwargs »", kwargs)

myfunc(1, 2, 3, 4, 5, kw1="ceva", alt_kw="ok ăsta unde se duce?")

# un argument keyword poate fi pasat ca pozițional
def myfunc(a, b, kw1="ceva"):
    print("a »", a)
    print("b »", b)
    print("kw1 »", kw1)

myfunc(1, 2, 3)

# dar putem să îl forțăm să fie pasat _doar_ ca keyword arg:
def myfunc(a, b, *, kw1="ceva"):
    print("a »", a)
    print("b »", b)
    print("kw1 »", kw1)

myfunc(1, 2) # works
myfunc(1, 2, 3) # fails!
myfunc(1, 2, kw1=3) # works

# un argument pozițional poate fi pasat ca keyword
def myfunc(a, b):
    print("a »", a)
    print("b »", b)

myfunc(b=2, a=1)

# dar putem să îl forțăm să fie pasat _doar_ ca positional arg:
def myfunc(a, b, /):
    print("a »", a)
    print("b »", b)

myfunc(a=1, b=2) # fails!
myfunc(1, 2) # works

# exemplu din standard library care implemetează și * și /
lst = [2, 3, 1]
sorted(iterable=lst) # fails
sorted(lst) # works
sorted(lst, lambda x: x) # fails
sorted(lst, key=lambda x: x) # works
