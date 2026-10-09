# generatorul este un caz particular de iterator

# iteratorul este un obiect ce suportă protocolul de iterare
# și execută cod pentru "returnarea" fiecărui element din iterație
# și își suspendă execuția între "returnări" (yield)

def myiter():
    print('1. intru în "funcție"')
    yield "value 1"
    print('2. sunt după primul yield')
    yield "value 2"
    print('3. sunt după al doilea yield')
    yield "value 3"
    print('ies din "funcție"')

it = myiter()
next(it)
next(it)
# ...


# Task: creați o funcție generator
# ce primește un iterabil cu numere
# și generează pătratele lor
def gensquares(it):
    for x in it:
        yield(x ** 2)

for elem in gensquares(range(50000000000000000000000000)):
    print(elem)

# să îl wrap-uim în alt generator
# și să observăm că este streaming data:
import time

def gensquares(it):
    for x in it:
        yield(x ** 2)
        time.sleep(.5)
        print('      --- sleeping a bit ---')

def filter_odd(it):
    for elem in it:
        if elem % 2:
            yield elem
        else:
            print('          dropped elem')

for elem in filter_odd(gensquares(range(5000000))):
    print(elem)


## generator expression (sintaxă de comprehension):

(x ** 2 for x in it)
# este echivalent cu:
def gensquares(it):
    for x in it:
        yield(x ** 2)

(elem for elem in it if elem % 2)
# este echivalent cu:
def filter_odd(it):
    for elem in it:
        if elem % 2:
            yield elem

gensquares = (x ** 2 for x in range(12000))
odd_elems = (elem for elem in gensquares if elem % 2)


# concepte:
# iter
# next

iterable = range(5) # could be whatever

for elem in iterable:
    print(elem)

# face de fapt:
iterable = range(5)
_it = iter(iterable)

while True:
    try:
        elem = next(_it)
    except StopIteration:
        # success! everything was iterated
        break
    else:
        print(elem)


### cu clase ###

# 1. pattern-ul complex:
# un iterabil, ce la iterație,
# returnează un iterator de altă clasă
class range_iterator:
    def __init__(self, num):
        self._next = 0
        self.num = num

    def __next__(self):
        next_value = self._next

        if next_value == self.num:
            raise StopIteration()

        self._next += 1

        return next_value

    # este întotdeauna o strategie bună
    # ca iteratorul să suporte și iter()
    # (și să se returneze pe sine)
    def __iter__(self):
        return self

class range:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return range_iterator(self.num)

# 2. pattern-ul cel mai des întâlnit:
# un obiect ce este deja iterator la instanțiere
# adică: suportă și __iter__ și __next__

class simplerange:
    def __init__(self, num):
        self._next = 0
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        next_value = self._next

        if next_value == self.num:
            raise StopIteration()

        self._next += 1

        return next_value


# protocolul de iterare este următorul:

# statement-ul for pe un obiect `obj`
# 1. cere crearea unui iterator din `obj`
#        adică it_obj = iter(obj)
# 2. pe acest obiect rulează în mod repetat
#        next()
# 3. dacă a apărut StopIteration
#    înseamnă că s-a încheiat cu succes iterația.

# aceste cuvinte aplicate în OOP înseamnă
# 1) clasa lui `obj` implementează __iter__
# 2) clasa lui `it_obj` implementează __next__

# și ultima bucată:
# `obj` poate să fie `it_obj`
#    adică iter(obj) să returneze tot pe obj

