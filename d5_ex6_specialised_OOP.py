# let's access items within an object

import random

class MyCollection:
    def __getitem__(self, key):
        if isinstance(key, slice):
            # some custom slicing code
            pass
        print("ai accesat cheia", key)
        return random.randint(1, 100)


class RealCollection:
    def __init__(self, items=None):
        if items is None:
            items = {}
        else:
            items = dict(items)

        self.__items = items

    def __getitem__(self, key):
        return self.__items[key]

    def __setitem__(self, key, value):
        self.__items[key] = value


# let's override attribute access

class CustomAccess:
    def __init__(self):
        self._hidden_stuff = {}

    # Atenție:
    # __getattr__ se rulează doar pt. atribute care nu există
    def __getattr__(self, name):
        try:
            return self._hidden_stuff[name]
        except KeyError:
            raise AttributeError()

    # Atenție:
    # __setattr__ se rulează pentru _tot_!
    def __setattr__(self, name, value):
        if name == '_hidden_stuff':
            super().__setattr__(name, value)

        self._hidden_stuff[name] = value

    # Atenție:
    # __getattribute__ se rulează pentru _tot_!
    def __getattribute__(self, name):
        print("»» accessing:", name)
        return super().__getattribute__(name)





# demonstrație de item access cu numpy:

import numpy
arr = numpy.array([

    ["a", "b", "c"],
    ["m", "n", "o"],
    ["x", "y", "z"],

])
# un index
arr[1]

# un slice = primele row-uri
arr[:2]

# acces x și y (în fapt o tuplă)
arr[1, 2]

# acces x și y unde x este slice
# deci tuplă(slice, index)
arr[:2, 2]

# exemplu explicit:
arr[ (  slice(None, 2), 2 )  ]

arr[ (  slice(None, 2), slice(1, None) )  ]
# adică
arr[:2, 1:]
