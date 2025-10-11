"""
Module de gestion de l'encodage UTF-8

Ce module fournit des fonctions pour encoder des caractères en UTF-8
et afficher différentes représentations (bytes, hexadécimal, décimal, binaire).
"""

from typing import List


def char_to_utf8_bytes(car: str) -> bytes:
    """
    Encode un caractère en UTF-8 et retourne les bytes bruts.
    
    Args:
        car (str): Le caractère à encoder
    
    Returns:
        bytes: La représentation en bytes UTF-8 du caractère
    
    Examples:
        >>> char_to_utf8_bytes('A')
        b'A'
        >>> char_to_utf8_bytes('é')
        b'\xc3\xa9'
    """
    return car.encode('utf-8')


def char_to_utf8_hex(car: str) -> str:
    """
    Encode un caractère en UTF-8 et retourne la représentation hexadécimale.
    
    Args:
        car (str): Le caractère à encoder
    
    Returns:
        str: La représentation hexadécimale des bytes UTF-8
    
    Examples:
        >>> char_to_utf8_hex('A')
        '41'
        >>> char_to_utf8_hex('é')
        'c3a9'
    """
    return car.encode('utf-8').hex()


def char_to_utf8_decimal(car: str) -> List[int]:
    """
    Encode un caractère en UTF-8 et retourne les valeurs décimales des octets.
    
    Args:
        car (str): Le caractère à encoder
    
    Returns:
        List[int]: Liste des valeurs décimales de chaque octet
    
    Examples:
        >>> char_to_utf8_decimal('A')
        [65]
        >>> char_to_utf8_decimal('é')
        [195, 169]
        >>> char_to_utf8_decimal('€')
        [226, 130, 172]
    """
    octets = car.encode('utf-8')
    return [octet for octet in octets]


def char_to_utf8_binary(car: str) -> str:
    """
    Encode un caractère en UTF-8 et retourne la représentation binaire.
    
    Args:
        car (str): Le caractère à encoder
    
    Returns:
        str: La représentation binaire des bytes UTF-8 (séparés par des espaces)
    
    Examples:
        >>> char_to_utf8_binary('A')
        '01000001'
        >>> char_to_utf8_binary('é')
        '11000011 10101001'
    """
    octets = car.encode('utf-8')
    return ' '.join(format(octet, '08b') for octet in octets)


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
    octets = char_to_utf8_decimal(car)
    
    print(f"Caractere : '{car}'")
    print(f"Octets UTF-8 : {octets}")


def string_to_utf8_info(text: str) -> dict:
    """
    Retourne un dictionnaire avec toutes les informations d'encodage pour une chaîne.
    
    Args:
        text (str): La chaîne à analyser
    
    Returns:
        dict: Dictionnaire contenant bytes, hex, decimal, binary
    
    Examples:
        >>> info = string_to_utf8_info("Bonjour")
        >>> print(info['hex'])
        '426f6e6a6f7572'
    """
    octets = text.encode('utf-8')
    
    return {
        'bytes': octets,
        'hex': octets.hex(),
        'decimal': [octet for octet in octets],
        'binary': ' '.join(format(octet, '08b') for octet in octets),
        'length': len(octets)
    }
