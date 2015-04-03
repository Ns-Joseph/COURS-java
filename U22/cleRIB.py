# -*- coding: utf-8 -*-

def calculeCleRIB(codeBanque, codeGuichet, codeCompte):
    reste = (89 * codeBanque + 15 * codeGuichet + 3 * codeCompte) % 97
    return 97 - reste 

codeBanque = int(raw_input("code banque : "))
codeGuichet = int(raw_input("code guichet : "))
codeCompte = int(raw_input("code compte : "))
cleRib = str(calculeCleRIB(codeBanque, codeGuichet, codeCompte))
print("La clé RIB est " + cleRib + ".")
