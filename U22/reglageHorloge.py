# -*- coding: utf-8 -*-

def distance(depart, arrivee, module):
    if (depart <= arrivee):
        return arrivee - depart
    else:
        return module + arrivee - depart
    
print ("Réglages actuels : ")
ah = int (input("* heures : "))
am = int (input("* minutes : "))
print ("Heure souhaitée : ")
bh = int (input("* heures : "))
bm = int (input("* minutes : "))
nombreDePressions = distance(ah, bh, 24) + distance(am, bm, 60)
print("Nombre de pressions : " + str(nombreDePressions)) 
