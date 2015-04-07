# -*- coding: utf-8 -*-

"""
Question 1 : 

1 + 3 + 5  + 7 = 16
"""

"""
Question 2 :

(version itérative)

Fonction sommeImpairs(n : entier) : entier
variables : 
      somme, terme, i : entier
début
    somme <- 0
    terme <- 1 
    Pour i allant de 1 à n 
        somme <- somme  + terme 
        terme <- terme + 2
    fpour
    retourner somme  
fin

ou bien (sans suite) :

Fonction sommeImpairs(n : entier) : entier
variables : 
      somme, i : entier
début
    somme <- 0
    Pour i allant de 1 à n 
        somme <- somme  + 2 * i - 1 
    fpour
    retourner somme  
fin

ou bien (version récursive) :

1 + 3 + 5 + 7 + ... + 13 + 15
= 15 + (1 + 3 + ... + 13)

Fonction sommeImpairs(n : entier) : entier
     Si n = 1 alors
        Retourner 1 
     sinon
        Retourner 2 * n - 1 +  sommeImpairs(n - 1)
     fsi
fin
"""

"""
Question 3 : 
"""

def sommeImpairs(n):
    somme = 0
    terme = 1
    for _ in range(0, n):
        somme += terme
        terme += 2
    return somme

"""
ou bien (version récursive) :
"""

def sommeImpairsRec(n):
    if n == 1 :
        return 1
    else :
        return 2 * n - 1 + sommeImpairsRec(n - 1)

"""
Question 4 : 
"""

for i in range(1, 21):
    print(str(i) + " : " + str(sommeImpairsRec(i)))

"""
Question 5 :

La somme des n premiers nombres impairs est n^2.

----> Preuve par récurrence :

* le premier nombre impair est 1, et 1^2 = 1, donc la propriété
est vraie pour n = 1.

* Montrons que si la somme des n premiers nombres impairs est n^2, 
alors la somme des n + 1 premiers nombres impairs est (n+1)^2.
Montrons que  (n+1)^2 = n^2 + 2 * (n + 1) - 1:
(n + 1)^2 = n^2 + 2 * n + 1 ^2 
= n^2 + (2 * n + 2 - 1)
= n^2 + 2 * (n + 1) - 1
Comme n^2 est la somme des n premiers nombres impairs 
(par hypothèse de récurrence), et que 2 * (n + 1) - 1 est le (n+1)ème 
nombre impair, alors n^2 + 2 * (n + 1) - 1
est la somme des (n+1) premiers nombres impairs.

----> Autre méthode 
(plus simple mais supposant la connaissance d'une formule) : 

La somme des termes consécutifs d'une suite arithmétique est donnée 
par : 

(premier + dernier) * nombreDeTermes / 2

soit, 

(1 + 2 * n - 1) * n / 2
= 2 * n * n / 2
= n^2
"""
