"""
from module import symbol
from module import symbol1, symbol2
from module import symbol as smb
from module import *

import module
import module as mod
"""

from os import path
import os.path

from os import path as p
import os.path as op

# toate sunt referință către același modul:
path is os.path is p is op


print("sunt în d5_ex1:", __name__)
import mymodule
# la import se execută main-body-ul modulului

# import-ul (mai precis execuția) se rulează
# o singură dată per lifetime-ul procesului
import mymodule

# mai puțin dacă ne băgăm degetele
import sys
del sys.modules['mymodule']
import mymodule


# un package este un director
import mypackage
#mypackage.submodule # nu există
from mypackage import submodule

# logica de modul a unui director se găsește în
# fișierul special "__init__.py"

print("» mypackage.submodule.SUB_VAR", mypackage.SUB_VAR)