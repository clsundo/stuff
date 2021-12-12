print("hello world !!!!")


def gg():
    while True:
        mot = input("Entrez quelque chose : ")
        if not mot:
            mot1 = input("Il faut entrer quelque chose merci : ")
            pass
            if not mot1:
                bye = input("Bye..")
                print(bye)
                break
            else:
                print(mot1)
                pass
        else:
            print(mot)
            pass


gg()
