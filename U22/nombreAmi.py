# -*- coding: utf-8 -*-

def sommeDiviseursStrict(n):
    somme = 0
    i = 1
    while 2 * i <= n :
        if n % i == 0 :
            somme += i 
        i += 1
    return somme

def trouveAmi(n):
    ami = sommeDiviseursStrict(n)
    if sommeDiviseursStrict(ami) == n:
        return ami
    return -1

def trouveAmis(nombre):
    n = 1
    while nombre > 0:
        ami = trouveAmi(n)
        if ami != -1 :
            if (ami == n):
                print(str(n) + " est parfait.")
            else:
                print(str(n) + " est ami avec " + str(ami) + ".")
            nombre -= 1
        n += 1
    
n = int(input("Saisissez un n : "))
ami = trouveAmi(n)
if (ami == -1):
    print(str(n) + " n'est ami avec aucun n.")
elif (ami == n):
    print(str(n) + " est ami avec lui-même, c'est donc un n parfait.")
else:
    print(str(n) + " est ami avec " + str(ami) + ".")

trouveAmis(10)