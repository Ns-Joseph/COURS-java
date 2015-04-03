def interpoleA(xa, ya, xb, yb):
    return (ya - yb)/(xa - xb)

def interpoleB(a, xa, ya):
    return ya - a * xa

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
