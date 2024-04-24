# correction_err.py
def lire_et_preparer_fichier(chemin_fichier: str) -> list:
    with open(chemin_fichier, 'r') as fichier:
        contenu = fichier.read().strip()  # Supprimer les espaces ou sauts de ligne éventuels
    # Convertir la chaîne de '0' et '1' en une liste de nombres binaires
    return [int(bit) for bit in contenu]


def calculer_et_corriger(c1: int, c2: int, c3: int, c4: int, c5: int, c6: int, c7: int) -> int:
    # Utilisation d'une approche directe pour le calcul des bits de parité
    p1, p2, p3 = c1 ^ c2 ^ c3, c1 ^ c2 ^ c4, c2 ^ c3 ^ c4
    
    # Utilisation de l'opérateur ternaire pour déterminer le code de correction
    correction = (
        1 if c5 != p1 and c6 != p2 and c7 == p3 else
        2 if c5 != p1 and c6 != p2 and c7 != p3 else
        3 if c5 != p1 and c6 == p2 and c7 != p3 else
        4 if c5 == p1 and c6 != p2 and c7 != p3 else
        0
    )
    return correction

def appliquer_correction(donnees: list) -> list:
    # Simplification de la boucle avec utilisation de slicing et enumerate
    corrige = []
    for idx in range(0, len(donnees), 7):
        code = calculer_et_corriger(*donnees[idx:idx+7])
        corrige.extend(
            (donnee ^ 1 if i + 1 == code else donnee for i, donnee in enumerate(donnees[idx:idx+7]))
        )
    return corrige

def extraire_donnees_utiles(donnees_corrige: list) -> list:
    # Simplification de la fonction d'extraction
    return [donnees_corrige[i] for i in range(len(donnees_corrige)) if i % 7 < 4]





      








