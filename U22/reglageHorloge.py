# -*- coding: utf-8 -*-

"""
Question 1 :

On doit faire passer les heures de 11 à 13 et les minutes de 22 à 15.
Pour les heures, on a 13 - 11 = 2 pressions, et pour les minutes, 
on fait (60 - 22) + 15 = 60 - 7 = 53. Le nombre total de 
pressions est donc 53 + 2 = 55.
"""

"""
Question 2 :

Algorithme réglage horloge

    Fonction additionHoraire(départ, arrivée, module : entier) : entier
    Début
        Si départ <= arrivée alors
               Retourner arrivée - départ
        sinon
            Retourner module + arrivée - départ
        fsi
    Fin 

Variables :
      h_A, m_A, h_B, m_B : entier
      nbPressions : entier

Début 
      Afficher "Saisir les heures puis les minutes de l'heure sur laquelle
                 le réveil est réglé"
      Saisir h_A, m_A
      Afficher "Saisir les heures puis les minutes de l'heure sur laquelle
                 vous souhaitez régler le réveil."
      Saisir h_B, m_B
      nbPressions <- additionHoraire(h_A, h_B, 24) + additionHoraire(m_A, m_B, 60)
      Afficher "Vous devrez effectuer ", nbPressions, " pressions."
Fin
"""

"""
Question 3 : 
"""

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

"""
Question 4 : 

Le pire cas s'obtient avec 23 pressions sur le bouton des heures et
59 fois sur le bouton des minutes, ce qui nous donne 23 + 59 = 82 
pressions. Par exemple, pour passer de 11:22 à 10:21.
"""