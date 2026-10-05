print("Hi from Earth!")

# Exercițiu:
# printați string-ul "Salut! "
# concatenat cu sine de 7 ori.

print("Salut! " * 7)


# Exercițiu:
# promptați utilizatorul pentru numele său
# și spuneți-i "Salut <nume>!!"
#name = input("Numele tău? ")

name = "Eu"

# v1: concatenare de stringuri
output = "Salut " + name + '!!'

# v2: formatare de string-uri "old-school" (printf)
output = "Salut %s" % name

# v3: formatare de string-uri tip template:
output = "Salut {name}".format(name=name)

# v4: folosind sintaxa de string formatting:
#     "f-string" (formatted string)
output = f"Salut {name}"

print(output)
