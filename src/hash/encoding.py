"""
Module de gestion de l'encodage UTF-8

Ce module fournit des fonctions pour encoder des caractères en UTF-8
et afficher différentes représentations (bytes, hexadécimal, décimal, binaire).
"""


def display_encoding_info(car: str) -> None:
    """
    Affiche l'encodage UTF-8 en octets pour un caractère donné.
    
    Args:
        car (str): Le caractère à analyser
    
    Examples:
        >>> display_encoding_info('A')
        Caractere : 'A'
        Octets UTF-8 : [65]
    """
    octets = car.encode('utf-8')
    decimal_values = [octet for octet in octets]
    
    print(f"Caractere : '{car}'")
    print(f"Octets UTF-8 : {decimal_values}")
