try:
    pass
except: # catch-all
    print("a fost excepție")

try:
    pass
finally: # folosit pentru clean-up
    print("se execută întotdeauna")

try:
    pass
except: # catch-all
    print("a fost excepție")
else: # se execută doar dacă nu a existat excepție
    print("totul ok")


# puse împreună:
try:
    pass
except:
    print("a fost excepție")
else:
    print("totul ok")
finally:
    print("se execută întotdeauna")

# except-urile, teoria completă:
# 1) putem avea mai multe branch-uri de except

try:
    pass
except IndexError:
    print("nu avem indexul")
except KeyError:
    print("nu avem cheia")
except:
    print("excepție neașteptată")

# 2) putem handle-ui mai multe tipuri de excepție
#    pe un singur branch:
try:
    pass
except (IndexError, KeyError):
    print("eroare de index sau cheie")

# 3) putem captura excepția:
try:
    pass
except IndexError as e:
    print(
        "avem o excepție",
        type(e),
        e
    )

# 4) putem să îi facem raise
try:
    pass
except IndexError as e:
    print("avem o excepție")
    # facem ceva specific aici

    # dar apoi lăsăm caller-ul
    # să se ocupe de problemă

    raise e

# putem să raise-uim o excepție custom oricând:
#raise IndexError("bad index")

# 4.1) de fapt nu este nevoie să capturăm excepția
#      ca să îi facem raise

try:
    pass
except:
    print("avem o excepție:")
    raise # va face re-raise excepției curente

# side-track despre raise:
# îl folosim unde și cum vrem
# pentru a comunica ceva "lateral"
# față de stream-ul normal de comunicare cu return
def myfunc(my_positive_int):
    if my_positive_int < 0:
        raise ValueError("give me a positive integer!")
    if int(my_positive_int) != my_positive_int:
        raise ValueError("give me int not float")

# 5. puse cap la cap,
#    și cu cazul capturării pe branch-ul de catch-all
try:
    pass
except IndexError:
    print("nu avem indexul")
except KeyError:
    print("nu avem cheia")
except Exception as e:
    print("excepție neașteptată", e)
else:
    print("totul ok")
finally:
    print("se execută întotdeauna")


# Task:
# reparăm acest cod astfel încât să nu facă overwrite
def copy(inpath, outpath, overwrite=False, chunk=8192):
    with open(inpath, "rb") as fin, open(outpath, "wb") as fout:
        while content := fin.read(chunk):
            fout.write(content)


import os.path

class FileExistsError(Exception):
    pass

def copy(inpath, outpath, overwrite=False, chunk=8192):
    # dacă nu avem voie să facem overwrite
    # și există fișierul outpath
    # trântim o excepție

    if overwrite is False and os.path.exists(outpath):
        # ne-am definit o excepție custom,
        # înseamnă că avem un protocol de comunicare via excepții
        # ce trebuie documentat pentru cine ne folosește api-ul
        raise FileExistsError("File exists, will not overwrite")

    with open(inpath, "rb") as fin, open(outpath, "wb") as fout:
        while content := fin.read(chunk):
            fout.write(content)

try:
    copy("orar.txt", "copie.txt")
except FileExistsError:
    print("este responsabilitatea caller-ului să trateze cu asta")
