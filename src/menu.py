"""
Module du menu principal du TP3

Ce module contient la fonction menu_principal qui gère l'interface utilisateur
et les choix des exercices.
"""

from src.exercises import (
    exercice_1_hachage_simple,
    exercice_2_collisions_et_preimages,
    exercice_3_hachage_texte,
    exercice_4_attaque_dictionnaire
)


def menu_principal() -> None:
    """
    Affiche le menu principal et gère les choix de l'utilisateur.
    """
    while True:
        print("\n" + "="*80)
        print("TP3 - Cryptographie - Fonctions de Hachage")
        print("="*80)
        print("1. Exercice 1 : Fonction de hachage H")
        print("2. Exercice 2 : Recherche de collisions et de préimages")
        print("3. Exercice 3 : Fonction de hachage H* pour texte")
        print("4. Exercice 4 : Attaque sur le dictionnaire")
        print("0. Quitter")
        print("="*80)

        choix = input("\nVotre choix : ").strip()

        if choix == '1':
            exercice_1_hachage_simple()
        elif choix == '2':
            exercice_2_collisions_et_preimages()
        elif choix == '3':
            exercice_3_hachage_texte()
        elif choix == '4':
            exercice_4_attaque_dictionnaire()
        elif choix == '0':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro entre 0 et 4.")