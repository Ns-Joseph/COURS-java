# -*- coding: utf-8 -*-

"""
Question 1 : 

Algorithme trouveAmis

    fonction sommeDiviseursStricts(n : entier) : entier
    variables : 
          somme, i : entier
    début
        somme <- 0
        Pour i <- 1 à (n-1) faire 
             Si n mod i = 0 alors
                 somme <- somme + i
             fsi
        pour
        Retourner somme
    fin

    fonction nombreAmi(n : entier) : entier
    variables :
          ami : entier
    début
        ami <- sommeDiviseursStricts(n)
        Si sommeDiviseursStricts(ami) = n alors
           Retourner ami
        sinon
           Retourner -1
        fsi     
    fin

variables : 
     nombre, ami : entier

Début
    Afficher "Saisissez un nombre"
    Saisir nombre
    ami <- nombreAmi(nombre)
    Si ami = -1 alors
       Afficher nombre, " n'a pas de nombre ami."
    sinon
       Afficher nombre, " est ami avec ", ami, "."
    fsi
Fin
"""

"""
Question 2 : 
"""

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

"""
On teste le code ci-dessus avec les instructions suivantes :

n = int(input("Saisissez un n : "))
ami = trouveAmi(n)
if (ami == -1):
    print(str(n) + " n'est ami avec aucun n.")
elif (ami == n):
    print(str(n) + " est ami avec lui-même, c'est donc un n parfait.")
else:
    print(str(n) + " est ami avec " + str(ami) + ".")
"""

"""
Question 3 :

L'instruction suivante nous donne le résultat : 284.
"""

print "220 est ami avec " + str(trouveAmi(220)) + "."

"""
Question 4 :

6 est ami avec lui-même, c'est un nombre parfait.
"""

print "220 est ami avec " + str(trouveAmi(6)) + "."

"""
Question 5 :
"""

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


trouveAmis(13)

"""
Résultat :
220 est ami avec 284.
220 est ami avec 6.
6 est parfait.
28 est parfait.
220 est ami avec 284.
284 est ami avec 220.
496 est parfait.
1184 est ami avec 1210.
1210 est ami avec 1184.
2620 est ami avec 2924.
2924 est ami avec 2620.
5020 est ami avec 5564.
5564 est ami avec 5020.
6232 est ami avec 6368.
6368 est ami avec 6232.
"""
