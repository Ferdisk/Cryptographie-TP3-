
from collision_preimages import H
def H_star(texte: str) -> int:
    """Fonction H* : XOR bit à bit de H(c) pour chaque caractère du texte"""
    h_total: int = 0  # Annotation explicite
    for c in texte:
        h_total ^= H(c)  # XOR
    return h_total
