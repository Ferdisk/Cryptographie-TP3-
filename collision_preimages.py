from typing import List, Tuple, Optional
import random

# Fonction de hachage modifiée pour générer des collisions
def H(car: str) -> int:
    # H(car) = (ord(car) * 10 + 7) % 20
    return (ord(car) * 10 + 7) % 20

# Tous les caractères ASCII imprimables
caracteres_possibles: List[str] = [chr(i) for i in range(33, 127)]

# Fonction qui trouve TOUTES les paires de collisions
def trouver_toutes_les_collisions():
    print("\n=== Recherche de TOUTES les paires de collisions ===")
    
    # Parcourir toutes les paires distinctes (c1, c2)
    # i pour c1 et j pour c2. j > i pour éviter les doublons et les comparaisons c1 == c1
    for i in range(len(caracteres_possibles)):
        for j in range(i + 1, len(caracteres_possibles)): 
            c1 = caracteres_possibles[i]
            c2 = caracteres_possibles[j]
            
            h1 = H(c1)
            h2 = H(c2)
            
            # Si les hachages sont identiques, c'est une collision
            if h1 == h2:
                # Afficher la collision
                print(f"'{c1}' et '{c2}' -> H = {h1}")

# Exemple d'exécution pour confirmer :
# trouver_toutes_les_collisions()
# Trouver une préimage aléatoire d'un caractère donné
def trouver_preimage_aleatoire(original: Optional[str] = None) -> Optional[Tuple[str, str, int]]:
    if original is None:
        original = random.choice(caracteres_possibles)
    h = H(original)
    # Cherche tous les autres caractères qui ont le même hachage
    candidats = [c for c in caracteres_possibles if H(c) == h and c != original]
    if candidats:
        preimage = random.choice(candidats)
        print(f"Original choisi : '{original}' -> H = {h}")
        print(f"Préimage différente trouvée : '{preimage}' -> H = {h}")
        return original, preimage, h
    else:
        print(f"Original choisi : '{original}' -> H = {h}")
        print("Aucune préimage différente trouvée.")
        return None