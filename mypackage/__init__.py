print("package-level logic")

PACKAGE_VAR = 22

# în momentul în care suntem într-un package
# avem acces la căi relative de module:
from . import submodule
# ^^ așa facem decă vrem să expunem un submodul
#    ca și cum a fost definit top-level

from .submodule import SUB_VAR
# ^^ am importat simbolul în namespace-ul curent.
#    așa facem când vrem să expunem top-level
#    doar câteva chestii importante din sub-module



