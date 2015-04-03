def sommeImpairs(n):
    somme = 0
    for i in range(0, n):
        somme += 2 * i + 1
    return somme

for i in range(1, 21):
    print(str(i) + " : " + str(sommeImpairs(i)))