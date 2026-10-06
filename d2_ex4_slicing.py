lst = ["ala", "bala", "ala", "porto", "cala"]

# slice între doi indecși:
lst[1:3]

# de la început, primele elemente:
lst[:3]

# de la indexul x, până la sfârșit:
lst[3:]

# cum luăm ultimele 3 elemente?
lst[-3:]

# cum luăm elementele de la început
# fără ultimele 2?
lst[:-2]

# și cu step:
# ținând cond că:
list(range(1, 20, 2))
# și
list(range(19, 0, -1))

# step în sintaxa de slicing:
lst[1:4:2]

# cum luăm fiecare al 2lea element din listă?
lst[::2]
