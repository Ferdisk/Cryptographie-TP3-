"""
Module de validation des entrées utilisateur

Ce module fournit des fonctions pour valider les caractères saisis par l'utilisateur
selon des critères spécifiques (alphanumérique ou caractères spéciaux autorisés).
"""

from typing import List, Optional


def is_valid_character(car: str, special_chars: Optional[List[str]] = None) -> bool:
    """
    Vérifie si un caractère est valide selon les critères définis.
    
    Un caractère est valide si :
    - Il a exactement 1 caractère de longueur ET
    - Il est une lettre ASCII (majuscule ou minuscule) OU il fait partie de la liste des caractères spéciaux autorisés
    
    Args:
        car (str): Le caractère à valider
        special_chars (List[str], optional): Liste des caractères spéciaux autorisés.
                                            Par défaut: ['!', '#', '(', ')', '*', '+', '/', '?']
    
    Returns:
        bool: True si le caractère est valide, False sinon
    
    Examples:
        >>> is_valid_character('A')
        True
        >>> is_valid_character('z')
        True
        >>> is_valid_character('#')
        True
        >>> is_valid_character('5')
        False
        >>> is_valid_character('@')
        False
        >>> is_valid_character('à')
        False
        >>> is_valid_character('AB')
        False
    """
    if special_chars is None:
        special_chars = ['!', '#', '(', ')', '*', '+', '/', '?']
    
    # Vérification de la longueur
    if len(car) != 1:
        return False
    
    # Vérification du type de caractère (lettre ASCII OU caractère spécial autorisé)
    return (car.isascii() and car.isalpha()) or car in special_chars


def validate_character(prompt: str = "Veuillez entrer un unique caractère : ",
                       error_prompt: Optional[str] = None,
                       special_chars: Optional[List[str]] = None) -> str:
    """
    Demande à l'utilisateur de saisir un caractère valide et valide l'entrée.
    
    Continue de redemander tant que l'entrée n'est pas valide.
    
    Args:
        prompt (str): Message affiché lors de la première demande
        error_prompt (str, optional): Message affiché en cas d'erreur. 
                                     Si None, un message par défaut est utilisé.
        special_chars (List[str], optional): Liste des caractères spéciaux autorisés
    
    Returns:
        str: Le caractère valide saisi par l'utilisateur
    
    Examples:
        >>> car = validate_character()
        Veuillez entrer un unique caractère : A
        >>> print(car)
        'A'
    """
    if special_chars is None:
        special_chars = ['!', '#', '(', ')', '*', '+', '/', '?']
    
    if error_prompt is None:
        chars_list = ' '.join(special_chars)
        error_prompt = (f"Veuillez entrer une unique lettre (majuscule ou minuscule) "
                       f"ou un des caractères spéciaux suivants {chars_list} : ")
    
    car: str = input(prompt)
    
    # Boucle de validation
    while not is_valid_character(car, special_chars):
        car = input(error_prompt)
    
    return car
