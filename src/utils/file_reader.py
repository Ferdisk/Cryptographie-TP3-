"""
Module de lecture de fichier texte

Ce module fournit des fonctions pour lire et extraire des caractères valides
depuis un fichier texte.
"""

from typing import List
from pathlib import Path
from .input_validator import is_valid_character


def read_valid_characters_from_file(file_path: str) -> List[str]:
    """
    Lit un fichier texte et extrait tous les caractères valides.
    
    Un caractère est considéré comme valide s'il est :
    - Une lettre (majuscule ou minuscule)
    - OU un des caractères spéciaux : !, #, (, ), *, +, /, ?
    
    Args:
        file_path (str): Chemin vers le fichier texte à lire
    
    Returns:
        List[str]: Liste des caractères valides trouvés dans le fichier
    
    Raises:
        FileNotFoundError: Si le fichier n'existe pas
        IOError: Si une erreur de lecture se produit
    
    Examples:
        >>> chars = read_valid_characters_from_file('ods5.txt')
        >>> 'a' in chars
        True
        >>> 'A' in chars
        True
        >>> '#' in chars
        True
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Le fichier {file_path} n'existe pas")
    
    valid_chars = set()  # Utiliser un set pour éviter les doublons
    special_chars = ['!', '#', '(', ')', '*', '+', '/', '?']
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Parcourir chaque caractère du fichier
            for char in content:
                if is_valid_character(char, special_chars):
                    valid_chars.add(char)
    
    except IOError as e:
        raise IOError(f"Erreur lors de la lecture du fichier : {e}")
    
    return sorted(list(valid_chars))  # Retourner une liste triée
