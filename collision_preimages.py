import random

def H(car: str) -> int:
    """Fonction de hachage simple (faible)"""
    return (ord(car) * 37 + 17) % 256

# Ensemble des caractères possibles
caracteres_possibles = [chr(i) for i in range(33, 127)]  # caractères imprimables ASCII

from typing import Dict, Tuple, Optional

def trouver_collision() -> Optional[Tuple[str, str, int]]:
    """Recherche empirique d'une collision"""
    hachages: Dict[int, str] = {}  # h : int, c : str
    for c in caracteres_possibles:
        h = H(c)
        if h in hachages:
            print(f"Collision trouvée : '{hachages[h]}' et '{c}' donnent tous deux {h}")
            return (hachages[h], c, h)
        hachages[h] = c
    print("Aucune collision trouvée.")
    return None


def trouver_preimage():
    """Recherche empirique d'une préimage"""
    car_choisi = random.choice(caracteres_possibles)
    h = H(car_choisi)
    print(f"Valeur hachée de '{car_choisi}' : {h}")
    for c in caracteres_possibles:
        if H(c) == h:
            print(f"Préimage trouvée : '{c}' donne aussi {h}")
            return (car_choisi, c, h)
    print("Aucune préimage trouvée.")
    return None

