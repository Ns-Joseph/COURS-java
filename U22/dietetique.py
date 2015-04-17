# -*- coding: utf-8 -*-

"""
Question 1 :

Considérons le tableau [1, 3, 2, 3, 1, 1, 2, 3, 1]. Commençons 
par calculer les effectifs :

[(1, 4), (3, 3), (2, 2)]

Le tableau ci-dessus contient des couples (valeur/effectif), 
trié par effectif décroissant.

Le 1, la valeur la plus fréquente, est sélectionnée pour être placée en 
première position. Le résultat est donc pour le moment [1, ...]. En mettant
à jour le tableau des effectifs, on a 

[(1, 3), (3, 3), (2, 2)]

L'effectif du 1 est devenu 1, vu qu'une boîte de pâtes a été retirée du 
placard. Cherchons ensuite la valeur la plus fréquente qui ne soit pas un 
1. La première rencontrée est un 3. Le résultat devient [1, 3, ...] et les 
effectifs deviennent [(1, 3), (3, 2), (2, 2)]

Les étapes suivantes sont résumées ci-dessous :
|------------------------------------------------------------| 
| résultat                        | effectifs                |
|------------------------------------------------------------| 
| [1, 3, 1, ...]                  | [(1, 2), (3, 2), (2, 2)] |
| [1, 3, 1, 3, ...]               | [(1, 2), (2, 2), (3, 1)] |
| [1, 3, 1, 3, 1, ...]            | [(2, 2), (1, 1), (3, 1)] |
| [1, 3, 1, 3, 1, 2, ...]         | [(2, 1), (1, 1), (3, 1)] | 
| [1, 3, 1, 3, 1, 2, 1, ...]      | [(2, 1), (3, 1), (1, 0)] | 
| [1, 3, 1, 3, 1, 2, 1, 2, ...]   | [(3, 1), (2, 0), (1, 0)] | 
| [1, 3, 1, 3, 1, 2, 1, 2, 3]     | [(3, 0), (2, 0), (1, 0)] |
|------------------------------------------------------------| 

(Remarquez que le deuxième tableau est maintenu 
trié par effectifs décroissants)

On obtient [1, 3, 1, 3, 1, 2, 1, 2, 3].
"""

"""
Question 2 : 

Nous utiliserons dans cette question un dictionnaire. C'est à dire un 
tableau dont les indices ne sont pas nécessairement contigus. Soit une 
variable d de type dictionnaire :
* d[i] est la valeur affectée à la clé i.
* d[i] est null si aucune valeur n'a été affectée à la clé i.
* taille(d) est le nombre de clés utilisées dans d. 
* cles(d) est l'ensemble des clés utilisées dans d, on peut par exemple
parcourir un dictionnaire avec la boucle 
    Pour chaque i dans cles(d)... 

procédure incrementeEffectif(effectifs : dictionnaire, valeur : entier)
    Si effectifs[valeur] = null alors
        effectifs[valeur] <- 1
    sinon
        effectifs[valeur] <- effectifs[valeur] + 1 
    fsi
fin

Nous aurons aussi besoin, de façon récurrente, d'échanger les éléments 
d'un tableau. Créons une procédure pour ce faire :

procédure echange(t : tableau de <T>, i, j : entier)
variable : 
    tmp : T
début
    tmp <- t[i]
    t[i] <- t[j]
    t[j] <- tmp    
fin

Nous utiliserons des couples (valeur, effectif) dans la question suivante.
Nous gérerons les couples avec une classe Marque contenant deux champs 
entier valeur et effectif. Le constructeur Marque (valeur, effectif) permettra
sera utilisé un peu plus loin.

Cette procédure est utile lorsque dans un  tableau trié par effectifs 
décroissants, un effectif a été décrémenté.

Procédure trieParEffectif(t : tableau de n Marque, i : entier)
    Tant que i < n - 1 et t[i].effectif < t[i + 1].effectif alors
        echange(t, i, i+1)
        i <- i + 1
    ftq
fin

L a fonction ci-dessous utilise un tableau de valeurs pour répertorier 
les marques et déterminer leur effectif. Elle prend en paramètre
un ensemble de valeurs et retourne un tableau de Marque précisant 
pour chaque valeur le nombre de fois où elle apparaît dans valeurs.

Le tableau retourné est trié par effectifs décroissants, des appels 
à la fonction trieParEffectif permettant d'effectuer un tri par insertion.

On se permet aussi de faire une allocation dynamique, c'est-à-dire de créer 
un tableau dont la taille se trouve dans une variable.

Fonction initialiseMarques(valeurs : tableau de b entiers) 
                            : tableau de Marques
Variables 
    t : tableau de Marques
    d : dictionnaire d'entiers
    i, p : entier
début
    Pour i <- 0 à n - 1
        incrementeEffectif(d, valeurs[i])
    fpour
    p <- taille(d)
    t <- tableau de p Marques
    i <- 0
    Pour chaque valeur dans cle(d)
        t[i] <- Marque (valeur, d[valeur])
        i <- i + 1
    fpour 
    Pour i <- p - 2 à 0
        trieParEffectifs(t, i)
    fpour
    retourner t
fin

La fonction suivante recherche dans effectifs la première marque m
vérifiant les conditions suivantes :
* m.valeur <> precedent
* m.effectif <> 0
En cas du succès, la valeur trouvée est retournée et t est mis à jour : 
* décrémentation de l'effectif de cette valeur.
* tri des effectifs pour préparer la prochaine recherce.
-1 est retourné si une telle marque n'existe pas.

Fonction trouveValeur(t : tableau de n Marque, precedent : entier):
Variables
    i : entier
Début
    i <- 0
    Tant que i < n et t[i].valeur = precedent
        i <- i + 1
    ftq
    Si i < n et  t[i].effectif <> 0 alors
        numero = t[i].valeur
        t[i].effectif <- t[i].effectif - 1
        trieParEffectif(t, i)
        return numero
    sinon
        return -1
    fsi
Fin

Nous pouvons maintenant assembler les sous-programmes pour 
mettre au point la procédure ordonne :

Procédure ordonne(valeurs : tableau de n entiers)
Variables
    marques : tableau de Marque
    i, suivant : entier
Début
    marques <- initialiseMarques(valeurs)
    i <- 0
    suivant <- trouveValeur(marques, -1)
    Tant que suivant <> -1
        valeurs[i] <- suivant
        suivant <- trouveValeur(marques, valeurs[i])
        i <- i + 1
    ftq
    Retourner i = n
Fin
"""

"""
Question 3 : 
"""

"""
Incrémente la valeur dont la clé est numéro dans le dictionaire effectifs.
Crée cette clé en lui attribuant la valeur 1 si elle 
n'existe pas. La procédure suivante décale l'objet d'indice i vers la droite 
du tableau jusqu'à ce qu'il soit suivi par un élément d'effectif inférieur.
"""

def incrementeEffectif(effectifs, valeur):
    if effectifs.has_key(valeur):
        effectifs[valeur] += 1
    else:
        effectifs[valeur] = 1

"""
Echange les éléments d'indices a et b dans liste.
"""

def echange(liste, a, b):
    tmp = liste[a]
    liste[a] = liste[b]
    liste[b] = tmp

"""
Echange l'élément d'indice i de la liste avec son successeur 
tant que l'effectif de i est inférieur à l'effectif de son 
successeur.
i est l'indice de l'élement à déplacer.
liste est un ensemble de couples (valeur, effectif).
A la fin de l'exécution de cette procédure, la liste doit être 
triée par effectifs décroissants.
"""

def trieParEffectif(liste, i):
    while i < len(liste) - 1 and liste[i][1] < liste[i + 1][1]:
        echange(liste, i, i+1)
        i += 1

"""
Recherche dans effectifs le premier couple (valeur, effectif)
vérifiant les conditions suivantes :
* valeur != precedent
* effectif != 0
En cas du succès, la valeur trouvée est retournée et le tableau des effectifs 
est mis à jour : 
* décrémentation de l'effectif de cette valeur.
* tri des effectifs pour préparer la prochaine recherce.
Non est retourné si un tel couple n'existe pas. 
"""

def trouveValeur(effectifs, precedent):
    i = 0
    while i < len(effectifs) and effectifs[i][0] == precedent:
        i += 1
    if i < len(effectifs) and effectifs[i][1] != 0:
        numero = effectifs[i][0]
        effectifs[i] = (effectifs[i][0], effectifs[i][1] - 1)
        trieParEffectif(effectifs, i)
        return numero
    else:
        return None

"""
Etant donné une liste "numéros", ordonne modifie l'ordre des éléments 
de la liste de sorte que deux numéros identiques ne soit pas côte-à-côte.
Retourne vrai en cas de succès, faux si un tel ordre n'existe pas.
"""

def ordonne(numeros):
    effectifs = {}
    for numero in numeros:
        incrementeEffectif(effectifs, numero)
    effectifsTries = list(effectifs.iteritems())
    effectifsTries.sort(key = lambda x : -x[1])
    i = 0
    suivant = trouveValeur(effectifsTries, None)
    while suivant != None:
        numeros[i] = suivant
        suivant = trouveValeur(effectifsTries, numeros[i])
        i += 1
    return (i == len(numeros))
        
boites = [1, 3, 2, 3, 1, 1, 2, 3, 1]
ordonne(boites)
print(boites)

"""
Question 4 :

Oui, elle ne fonctione pas avec [1, 1]

Plus généralement elle ne fonctionne pas si : 

(1) il existe i tel que 
effectif(i) > somme_{j <> i} effectifs(j) + 1 

Donc s'il existe une boîte en plus grande quantité que toutes les
autres boîtes réunies + 1. 

En effet, si la condition (1) est vraie, il est impossible pour un algorithme
de réussir car deux boîtes de même numéro se trouveront nécessairement côte
à côte. Cela peut se montrer par récurrence. 
"""

"""
Question 5 :

Il existe un moyen de procéder plus rapidement en utilisant un 
tas pour stocker les marques. Mais la question la plus intéressante 
à se poser est existe-t-il un algorithme qui réussit là où celui-ci échoue.

Or, cet algorithme n'échoue que lorsqu'il n'y a pas du tout de solution.

En effet, si la condition (1) de la question précente est fausse, l'algorithme
fonctionera correctement. On s'en convainc en constatant que si un numéro 
apparaît en grande quantité, il occupera une case sur deux dans le résultat.

Par conséquent il n'y en a pas de meilleur.  
"""