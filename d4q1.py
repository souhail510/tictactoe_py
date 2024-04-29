#Souhail Daoudi
#Anis Rahmouni El idrissi
def ajoute (matrice):
    "modifie la matrice en ajoutant 1 à tous les éléménts"
    i=0
    matriceModifiée=[]
    while i<len(matrice):
        j=0
        matriceModifiée.append([])
        while j<len(matrice[i]) :
            c=matrice[i][j]+1
            matriceModifiée[i].append(c)
            j=j+1
        i=i+1
    return matriceModifiée

def ajoute_V2 (matrice):
    "retourne une nouvelle matrice contenant les valeurs de la matrice donnée comme paramètre incrémenté avec 1, sans la modifier"
    NouvelleMatrice= ajoute(matrice)
    return NouvelleMatrice

print("Entrez les nombres avec des espaces entre les colonnes.")
print("Une rangee par ligne, et une ligne vide a la fin.")
matrice = []
while True:
    ligne = input()
    if not ligne: break
    valeurs = ligne.split()
    rangee = [int(val) for val in valeurs]
    matrice.append(rangee)
    
print("la matrice est:")
print(matrice)
matriceModifiée=ajoute (matrice)
print("Apres exécution de la fonction ajoute, la matrice est:")
print(matriceModifiée)
print("Une nouvelle matrice créée avec ajoute_V2:")
print(ajoute_V2(matriceModifiée))
print("Apres exécution de la fonction ajoute_V2, la matrice initiale est:")
print(matriceModifiée)
