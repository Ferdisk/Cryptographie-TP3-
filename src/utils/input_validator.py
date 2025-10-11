"""
Module de validation des entrées utilisateur

Ce module fournit des fonctions pour valider les caractères saisis par l'utilisateur
selon des critères spécifiques (alphanumérique ou caractères spéciaux autorisés).
"""

from typing import List


def is_valid_character(car: str, special_chars: List[str] = None) -> bool:
    """
    Vérifie si un caractère est valide selon les critères définis.
    
    Un caractère est valide si :
    - Il a exactement 1 caractère de longueur ET
    - Il est une lettre (majuscule ou minuscule) OU il fait partie de la liste des caractères spéciaux autorisés
    
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
        >>> is_valid_character('AB')
        False
    """
    if special_chars is None:
        special_chars = ['!', '#', '(', ')', '*', '+', '/', '?']
    
    # Vérification de la longueur
    if len(car) != 1:
        return False
    
    # Vérification du type de caractère (lettre OU caractère spécial autorisé)
    return car.isalpha() or car in special_chars


def validate_character(prompt: str = "Veuillez entrer un unique caractère : ",
                       error_prompt: str = None,
                       special_chars: List[str] = None) -> str:
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


def validate_character_verbose(special_chars: List[str] = None) -> str:
    """
    Version verbeuse de validate_character avec des messages détaillés.
    
    Args:
        special_chars (List[str], optional): Liste des caractères spéciaux autorisés
    
    Returns:
        str: Le caractère valide saisi par l'utilisateur
    """
    if special_chars is None:
        special_chars = ['!', '#', '(', ')', '*', '+', '/', '?']
    
    car: str = input("Veuillez entrer un unique caractère : ")
    
    while len(car) != 1 or (not car.isalpha() and car not in special_chars):
        chars_list = ' '.join(special_chars)
        car = input(f"Veuillez entrer une unique lettre (majuscule ou minuscule) "
                   f"ou un des caractères spéciaux suivants {chars_list} : ")
    
    return car
