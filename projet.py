#Hallouche Mehdi





import pandas as pd

# Données : Séquences ADN, Longueur, Pourcentage de GC
data = {
    "Séquence": ["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
    "Longueur": [12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}

# Création d'un DataFrame
df = pd.DataFrame(data)

print("**************** Creation et affichage *****************")
print("Tableau des séquences ADN :")
print(df)
print("*****************affichege de longueur************ ")
# Sélectionner la colonne "Longueur"
longueur = df["Longueur"]
print(longueur)
#3)Filtrer les séquences avec une longueur superieur à 10
print("************* Filtrage avec longueur >10 *************")
filtered_df = df[df["Longueur"] > 10]
print(filtered_df)
#4)la moyenne de pourcentage GC 
print("**************moyenne de pourcentage GC%**************")
average_GC=df["Pourcentage GC"].mean()
print(f"Pourcentage GC : {average_GC:.3f}")
#5)Ajouter une nouvelle colonne avec 
print("************* Ajout d'une nouvelle colonne *************")
# Ajouter une nouvelle colonne "categorie pourcentage"
df["Catégorie Pourcentage GC"] = df["Pourcentage GC"].apply(lambda x: "riche" if x > 55 else ("moyen" if 45 <= x <= 55 else "faible"))
print(df)
