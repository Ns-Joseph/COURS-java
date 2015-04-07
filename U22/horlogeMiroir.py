# -*- coding: utf-8 -*-

"""
Question 1 : 

Il est 10:23
"""

"""
Question 2 :

Fonction miroirAiguille(position, module : entier) : entier
Debut
    Retourner (module - position) modulo module
Fin 

ou bien 

Debut
    Si position = 0 alors
       Retourner 0
    Retourner  module - position
Fin 

Procédure miroirHorloge(heures, minutes : entier)
      Afficher "Il est ", miroirAiguille(heures, 12), ":", miroirAiguille(minutes, 60)
Fin
"""

"""
Question 3 : 
"""

def miroirAiguille(position, module):
    if position == 0 :
        return 0
    return module - position

print("Lisez l'heure dans le miroir : ")
h = int (input("* heures : "))
m = int (input("* minutes : "))
h = miroirAiguille(h, 12)
m = miroirAiguille(m, 60)
print("Il est " + str(h) + ":" + str(m) + ".")

"""
Question 4 : 

Lorsqu'une aiguille est positionnée vers le haut (12 heures) ou le bas (6 heures), 
elle apparaît au même emplacement vue dans un miroir. Comme l'aguille
des minutes indique 0 lorsque l'aiguille est positionnée en haut et 30
en bas, les heures heures "symétriques" de la journée sont :
* 00:00
* 00:30
* 6:00
* 6:30
"""
