import os

def est_premier(nombre):
    # Fonction pour vérifier si un nombre est premier
    if nombre < 2:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True

def generer_nombre_premier(ensemble_premiers):
    # Fonction pour générer un nombre premier unique
    candidat_premier = 2
    while True:
        # Vérifie si l element est un nombre premier et s'il n'est pas déjà dans l'ensemble
        if est_premier(candidat_premier) and candidat_premier not in ensemble_premiers:
            ensemble_premiers.add(candidat_premier)
            return candidat_premier
        candidat_premier += 1

nombre_cles_a_generer = 1000000
dossier_sortie = "dossier_cles256"
chemin_fichier_premiers = "premiers256.txt"

# Crée le dossier pour stocker les clés s'il n'existe pas
os.makedirs(dossier_sortie, exist_ok=True)

# Stocke les nombres premiers dans un ensemble pour éviter les doublons
ensemble_premiers = set()

# Génère les nombres premiers et les clés RSA directement dans le dossier spécifié
with open(chemin_fichier_premiers, "w") as fichier_premiers:
    for i in range(nombre_cles_a_generer):
        # Génère deux nombres premiers (p et q) pour chaque clé RSA
        premier_p = generer_nombre_premier(ensemble_premiers)
        premier_q = generer_nombre_premier(ensemble_premiers)

        # Stocke p et q dans le fichier premiers.txt
        fichier_premiers.write(f"{premier_p} {premier_q}\n")

        # Génère une clé RSA de 256 bits et la stocke dans un fichier texte
        chemin_fichier_cle = os.path.join(dossier_sortie, f"cle_{i}.txt")
        os.system(f"openssl genrsa 256 > {chemin_fichier_cle}")

# Affiche le résultat de l'opération
print(f"{nombre_cles_a_generer} clés générées avec succès dans le dossier {dossier_sortie}")
print(f"Nombres premiers stockés dans {chemin_fichier_premiers}")

