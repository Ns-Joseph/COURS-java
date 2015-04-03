def miroirAiguille(position, module):
    return module - position

print("Lisez l'heure dans le miroir : ")
h = int (input("* heures : "))
m = int (input("* minutes : "))
h = miroirAiguille(h, 12)
m = miroirAiguille(m, 60)
print("Il est " + str(h) + ":" + str(m) + ".")
