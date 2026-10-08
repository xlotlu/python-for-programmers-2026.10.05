# decoratorul este o funcție
# ce primește ca unic argument o funcție
# și returnează o altă funcție

def decofunc(func):
    pass

@decofunc
def myfunc():
    pass
# este "syntactic sugar" pentru:
def myfunc():
    pass
myfunc = decofunc(myfunc)

from functools import cache
import random

def myfunc(a, b):
    return random.randint(a, b)
myfunc = cache(myfunc)

# echivalent cu:
@cache
def myfunc(a, b):
    return random.randint(a, b)

@cache
def crazy_long_running_func(param):
    return rezultat_deterministic_pt_param

# use-case-uri pentru decoratori:
# - schimbăm data-type-ul output-ului
#   (exemplu: în loc de dict generăm json)
# - timing al execuției
# - facem logging cu tot ce s-a executat
# - retry execution
# - cache


# First, there was the factory...
#def pow(x, y):
#    return x ** y
def mkpow(exp):
    def _the_pow_func(x):
        return x ** exp
    return _the_pow_func

pow_3 = mkpow(3)
pow_5 = mkpow(5)

pow_3(2)

# In the meantime...
# funcs can be passed as params!
def apply(func, param):
    return func(param)

apply(pow_5, 2)


def pow(x, y):
    return x ** y

from functools import partial
pow_3 = partial(pow, y=3)

# almost full-circle:
# partial: receives a function,
#          returns a function

# Full-circle:
# how about we receive a function f,
# return another function f'
# that does something extra around f.

def mywrapper(f):
    def _inner():
        print("»» I am now inside the deco!")
        result = f()
        print("»» I executed f!")
        return result
    return _inner

def myfunc():
    print("» I am the real function")
    return 42

wrapped_func = mywrapper(myfunc)

# and the icing on the cake:
# instead of
myfunc = mywrapper(myfunc)

# let's give it a special syntax:
@mywrapper
def myfunc():
    print("» I am the real function")
    return 42

# but what about the arguments?!?
def mywrapper(f):
    def _inner(*args, **kwargs): # "argument packing"
        print("»» I am now inside the deco!")

        result = f(*args, **kwargs) # "argument unpacking"

        print("»» I executed f!")
        return result
    return _inner

@mywrapper
def myfunc(x, y="to infinity and beyond"):
    print("» I am the real function")
    print(f'» with x: {x} and y: {y}')
    return 42

# despre argument unpacking:
lst = ["ala", "bala", "porto"]
print(*lst, sep=' // ')
# este echivalent cu:
print("ala", "bala", "porto", sep=' // ')


# Exercițiu:
# pornind de la `mywrapper()` de mai sus
# scrieți un decorator
def timeit(func):
    pass
# ce printează durata de execuție a funcției decorate

# exemplu minimal-minimal-minimal
def deco(func):
    def _inner(*args, **kwargs):
        # aici pot să fac chestii înainte
        result = func(*args, **kwargs)
        # aici pot să fac chestii după
        return result
    return _inner

from datetime import datetime
def timeit(func):
    def _inner(*args, **kwargs):
        start = datetime.now()

        result = func(*args, **kwargs)

        end = datetime.now()

        print(f"» Execution took: {(end - start).total_seconds()} s")
        return result
    return _inner

from time import sleep

@timeit
def mysleepy():
    sleep(.001)
    return "something"

mysleepy()

# Exercițiu:
# Scrieți un decorator
def logit(func):
    pass
# ce printează numele funcției,
# valorile argumentelor primite,
# și rezultatul execuției

import sys
import time

LOG_TEMPLATE = "{time_ms:.04f}ms :: {module}.{function}({args}) -> {result}"
def logit(func):
    def _inner(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        _all_args = [
            repr(arg)
            for arg in args
        ] + [
            f'{k}={repr(v)}'
            for k, v in kwargs.items()
        ]

        print(
            LOG_TEMPLATE.format(
                module=__name__,
                function=func.__qualname__,
                args=", ".join(_all_args),
                result=repr(result),
                time_ms=(end - start) * 1000,
            ),
            file=sys.stderr
        )

        return result
    return _inner

@logit
def myfunc(a, b, kw=1, xkw="nothing"):
    time.sleep(.001)
    return a * b * kw