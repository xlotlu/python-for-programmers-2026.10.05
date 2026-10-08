# Essential concepts

Python: interpretat

executabilul python este și o aplicație REPL
"read - eval - print - loop"

în Python *totul* este un obiect


Python este pentru productivity
Python nu este pentru performanță,
    DAR pot fi împăcate amândouă:
    - python pt. main program
    - un modul în C / rust pt. lucruri f. specializate

în Python nu există "fundamental data types"
 -> pentru că totul este un obiect
    -> deci totul este o instanță a unei clase
       -> deci dacă vrem să facem type casting
          apelăm clasa respectivă cu argumentul dorit.


în Python, _totul_ poate fie evaluat în context boolean

în Python totul este o referință!


în Python orice operator rulează de fapt
un "dunder method" specific.

exemplu:
  == __eq__
  >  __gt__
  <  __lt__
  +  __add__
  -  __sub__


## Alte concepte:

reprezentare = felul în care arată un obiect când este inspectat

iterabil = orice obiect care poate fi iterat (folosit în `for`)

iterator = un iterabil foarte specific ce este conștient
           de starea curentă a iterației, și poate genera
           valori la runtime.
           implicație: nu are nevoie să fie memory-backed.


# Things you should read at least once

the styleguide:
https://peps.python.org/pep-0008/

PEP = Python Enhancement Proposal

string formatting:
https://docs.python.org/3/library/string.html#format-examples

datetime formatting and parsing:
https://docs.python.org/3/library/datetime.html#format-codes


# Other language specifics:

## Operatori:

Noi întâlniți:

// partea întreagă
%  restul împărțirii
** ridicare la putere

[!] operatorul depinde de context
    (adică data-type-ul pe care operează decide ce înseamnă pentru el)

operatori suportați de `str`:

```
+ * %
```

## Escape sequences:

\n newline
\r carriage return
\t tab

mai puțin importante, dar să nu vă ia prin surprindere:

\u011b caracter unicode, ce poate fi reprezentat cu 4 hexadecimale
\U0001D11E caracter unicode, ce poate fi reprezentat cu mai mult de 4 hexadecimale
"\N{latin capital letter a}" între acolade numele caracterului conform standardului unicode
"\x4e" byte-ul 4E (hex). pt. valori < 128 corespunde unui caracter din tabelul ascii 


# Essential debugging tools

print()
help()
type()


# datatype-uri

## datatype-uri de bază:

- int
- float
- bool
- str
- tuple # immutable
- list  # mutable
- dict  # mutable
- set   # mutable

## sequences

str, list, tuple

- sunt iterabile cu for
- au lungime: funcționează len()
- sunt accesibile după index
- suportă slicing
- au metodele .count() și .index()


# Excepții importante:

ValueError: generică, atunci când valoarea primită este ne-conformă
TypeError: când o funcție primește argumente invalide (număr invalid, nume invalide)
NameError: simbolul (variabila, funcția etc.) nu este definit

SyntaxError
IndentationError

IndexError: când operăm (pe o listă, alte sequences, și alte obiecte cu index access)
            și indexul respectiv nu există
KeyError:   când nu există cheia respectivă

AttributeError: nu este definit atributul accesat pe acest obiect

# Very useful packages

(pip install)

ipython
ipdb
rich

# Random things:

părerea lui Ionuț: criteriile pt. cod bun, în ordine:
- readability (whitespace, nume de variabile și funcții)
- eleganță (non-dens, non-complicat, în timp ce poate să fie complex)
- performanță


There are 2 most difficult things in computing:
- naming things
- cache invalidation
- off-by-one errors

There are 10 types of people, those that understand binary and those that don't.

https://xkcd.com/231/
