# -*- coding: utf-8 -*-

def ajoute(effectifs, numero):
    if effectifs.has_key(numero):
        effectifs[numero] += 1
    else:
        effectifs[numero] = 1

def swap(liste, a, b):
    tmp = liste[a]
    liste[a] = liste[b]
    liste[b] = tmp

def deplacerEffectif(liste, i):
    while i < len(liste) - 1 and liste[i][1] < liste[i + 1][1]:
        swap(liste, i, i+1)
        i += 1
    
def trouveSuivant(effectifs, precedent):
    i = 0
    while i < len(effectifs) and effectifs[i][0] == precedent:
        i += 1
    if i < len(effectifs) and effectifs[i][1] != 0:
        numero = effectifs[i][0]
        effectifs[i] = (effectifs[i][0], effectifs[i][1] - 1)
        deplacerEffectif(effectifs, i)
        return numero
    else:
        return None

def ordonne(numeros):
    effectifs = {}
    for numero in numeros:
        ajoute(effectifs, numero)
    effectifsTries = list(effectifs.iteritems())
    effectifsTries.sort(key = lambda x : -x[1])
    i = 0
    precedent = None
    suivant = trouveSuivant(effectifsTries, None)
    while suivant != None:
        numeros[i] = suivant
        precedent = suivant
        suivant = trouveSuivant(effectifsTries, precedent)
        i += 1
    if (i != len(numeros)):
        print("Pas de solution complète.")
    
boites = [1, 3, 2, 3, 1, 1, 2, 3, 1]
ordonne(boites)
print(boites)
