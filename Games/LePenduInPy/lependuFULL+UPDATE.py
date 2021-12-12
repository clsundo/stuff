import random
import time
import sys

# delay print (dependance time, sys)
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)

# Choisi un mot (dependence random)
# Nécessite un fichier mots.txt dans le répertoir du script
mots = []
with open("mots.txt") as fl:
    for l in fl:
        mots.append(l.rstrip("\n"))
mot = random.choice(mots)

# Variable cle
lettres = []
faux = 0
trouve = False
corp_plein = ["|", "+---+", "|", "O", "/", "|", "\\", "/", "\\"]
corp = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

while not trouve:
    trouve = True
    print(" {}".format(corp[1]))
    print(" {}   {}".format(corp[0], corp[2]))
    print(" {}   {}".format(corp[0], corp[3]))
    print(" {}  {}{}{}".format(corp[0], corp[4], corp[5], corp[6]))
    print(" {}  {} {}".format(corp[0], corp[7], corp[8]))
    print("_|_")
    print("| |")
    for l in mot:
        if l in lettres:
            print(l, end=" ")
        else:
            trouve = False
            print("_", end=" ")
    print()
    print("Lettres utilisees - ", end="")
    for l in lettres:
        print(l, end=" | ")
    print()

    if faux > 8:
        delay_print("Tu as perdu! :(\n")
        input("Le mot était -> {}".format(mot))
        break
    
    if trouve:
        delay_print("Tu as gagne! :)\n")
        input(":D")
        break

    lettre = input("Entez une lettre: ")
    if lettre not in lettres:
        lettres.append(lettre)
    else:
        delay_print("Lettre déjà utilisée\n")

# Si la lettre choisis n'est pas dans le mot 
    if lettre not in mot:
        corp[faux] = corp_plein[faux]
        faux += 1