# -*- coding: utf-8 -*-

"""
Question 1 :

On cherche a et b tels que y = ax + b pour les deux points 
A(0, 1) et B(1, 2). Donc nous devons avoir :
    1 = a * 0 + b
et  2 = a * 1 + b
 
D'après la première équation, b = 1. Remplaçons-le dans
la deuxième : 
    2 = a * 1 + 1
<=> 1 = a
Donc, l'équation est y = x + 1.

Autre méthode :

Le coefficient directeur a est donné par : (1 - 2)/(0 - 1) = 1, 
Remplaçons a par 1 dans la première équation :
        1 = 1 * 0 + b
<=>     b = 1
"""

"""
Question 2 :

a = (y_B - y_A)/(x_B - x_A)
"""

"""
Question 3 : 

Exprimons b en fonction de a, x_A et y_A en utilisant la formule 
y = ax + b. On a 

               y = ax + b
<=>    y - ax  = b
<=>    b = y - ax. 

Remplaçons x et y par les coordonnées
de A, il vient b = y_A - a * x_A.
"""

"""
Question 4 : 

fonction interpoleA(x_A, y_A, x_B, y_B : réel) : réel
début
    Retourner (y_B - y_A)/(x_B - x_A)
fin

fonction interpoleB(a, x_A, y_A : réel) : réel
début
    Retourner y_A - a * x_A.
fin
"""

"""
Question 5 : 
"""

def interpoleA(xa, ya, xb, yb):
    return (ya - yb)/(xa - xb)

"""
Question 6 : 
"""

def interpoleB(a, xa, ya):
    return ya - a * xa

"""
Question 7 : 

interpoleA ne pourra pas s'exécuter en cas de division par 
zéro. Donc si x_B - x_A = 0 <=> x_A = x_B. Autrement dit, 
si les deux points sont alignés verticalement.
"""

xa = int (input("xa : "))
ya = int (input("ya : "))
xb = int (input("xb : "))
yb = int (input("yb : "))

if (xa == xb):
    if (ya == yb):
        print("Les deux points sont confondus.")
    else:
        print("x = " + str(xa))
else:
    if (ya == yb):
        print("y = " + str(ya))
    else:
        a = interpoleA(xa, ya, xb, yb)
        b = interpoleB(a, xa, ya)
        print("y = " + str(a) + "*x + " + str(b))
