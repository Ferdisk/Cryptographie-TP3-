"""
Programme principal du TP3 - Hachage Cryptographique

Ce programme démontre l'utilisation des fonctions de hachage cryptographique
et de l'encodage UTF-8 sur des caractères issus d'un fichier texte.
"""

import sys
from pathlib import Path

# Ajouter le répertoire parent au PYTHONPATH pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils.input_validator import validate_character, is_valid_character
from src.utils.file_reader import read_valid_characters_from_file
from src.hash.encoding import display_encoding_info
from src.hash.hash_functions import display_all_hashes, compare_hashes

# Chemin du fichier texte contenant les caractères
FICHIER_TEXTE = "ods5.txt"


def menu_principal() -> None:
    """
    Affiche le menu principal et gère les choix de l'utilisateur.
    """
    while True:
        print("\n" + "="*80)
        print("TP3 - Cryptographie - Fonctions de Hachage")
        print("="*80)
        print("1. Exercice 1 : Fonction de hachage H")
        print("2. Exercice 2 : Recherche de collisions")
        print("3. Exercice 3 : Recherche de préimages")
        print("4. Exercice 4 : Fonction de hachage H* pour texte")
        print("5. Exercice 5 : Attaque sur le dictionnaire")
        print("0. Quitter")
        print("="*80)
        
        choix = input("\nVotre choix : ").strip()
        
        if choix == '1':
            exercice_1_hachage_simple()
        elif choix == '2':
            exercice_2_collisions()
        elif choix == '3':
            exercice_3_preimages()
        elif choix == '4':
            exercice_4_hachage_texte()
        elif choix == '5':
            exercice_5_attaque_dictionnaire()
        elif choix == '0':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro entre 0 et 5.")


def mode_encodage() -> None:
    """
    Mode d'affichage de l'encodage UTF-8 d'un caractère.
    Utilise un caractère du fichier texte ou saisi par l'utilisateur.
    """
    print("\n" + "-"*80)
    print("MODE : ENCODAGE UTF-8")
    print("-"*80)
    
    print("\n1. Utiliser un caractere du fichier texte")
    print("2. Saisir un caractere manuellement")
    choix = input("\nVotre choix : ").strip()
    
    if choix == '1':
        try:
            chars = read_valid_characters_from_file(FICHIER_TEXTE)
            print(f"\nCaracteres disponibles ({len(chars)} au total)")
            print("Affichage des 50 premiers : " + ", ".join(f"'{c}'" for c in chars[:50]))
            
            index_str = input(f"\nEntrez l'index du caractere (0-{len(chars)-1}) : ")
            index = int(index_str)
            
            if 0 <= index < len(chars):
                car = chars[index]
                print(f"\nCaractere selectionne : '{car}'")
                print()
                display_encoding_info(car)
            else:
                print(f"Erreur : Index hors limites (0-{len(chars)-1})")
        except (FileNotFoundError, IOError) as e:
            print(f"Erreur : {e}")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide")
    elif choix == '2':
        car = validate_character()
        print("\n")
        display_encoding_info(car)
    else:
        print("Choix invalide")


def mode_hash() -> None:
    """
    Mode de calcul des hash d'un caractère.
    """
    print("\n" + "-"*80)
    print("MODE : CALCUL DES HASH")
    print("-"*80)
    
    car = validate_character()
    display_all_hashes(car)


def mode_comparaison() -> None:
    """
    Mode de comparaison des hash de deux caractères.
    """
    print("\n" + "-"*80)
    print("MODE : COMPARAISON DE HASH")
    print("-"*80)
    
    print("\nPremier caractère :")
    car1 = validate_character()
    
    print("\nDeuxième caractère :")
    car2 = validate_character()
    
    compare_hashes(car1, car2)


def mode_interactif_complet() -> None:
    """
    Mode interactif complet : affiche encodage ET hash.
    """
    print("\n" + "-"*80)
    print("MODE : ANALYSE COMPLETE")
    print("-"*80)
    
    car = validate_character()
    
    print("\n" + "="*80)
    print("ANALYSE COMPLETE DU CARACTERE")
    print("="*80)
    
    # Encodage
    print("\nENCODAGE UTF-8 :")
    print("-"*80)
    display_encoding_info(car)
    
    # Hash
    print("\nFONCTIONS DE HACHAGE :")
    print("-"*80)
    display_all_hashes(car)


def exercice_1_hachage_simple() -> None:
    """
    Exercice 1 : Fonction de hachage H
    Affiche l'encodage UTF-8 d'un caractère (1 octet)
    """
    print("\n" + "-"*80)
    print("EXERCICE 1 : FONCTION DE HACHAGE H")
    print("-"*80)
    print("Saisissez un caractère parmi : lettres (a-z, A-Z) ou caractères spéciaux (!, #, (, ), *, +, /, ?)")
    print("La fonction H retourne l'encodage UTF-8 du caractère (valeur entre 20 et 80).")
    
    car = validate_character()
    print(f"\nCaractère saisi : '{car}'")
    print()
    display_encoding_info(car)


def exercice_2_collisions() -> None:
    """
    Exercice 2 : Recherche de collisions
    Essaie de trouver deux caractères différents qui donnent la même valeur hachée
    """
    print("\n" + "-"*80)
    print("EXERCICE 2 : RECHERCHE DE COLLISIONS")
    print("-"*80)
    print("Recherche de deux caractères différents qui donnent la même valeur hachée...")
    
    # Liste de tous les caractères ASCII imprimables pour la démonstration
    tous_caracteres = []
    for code in range(32, 127):  # Caractères ASCII imprimables
        car = chr(code)
        tous_caracteres.append(car)
    
    print(f"Nombre total de caractères ASCII imprimables : {len(tous_caracteres)}")
    
    # Créer un dictionnaire valeur_hachee -> liste de caractères pour TOUS les caractères
    hachages_tous = {}
    for car in tous_caracteres:
        hache = car.encode('utf-8')[0]
        if hache not in hachages_tous:
            hachages_tous[hache] = []
        hachages_tous[hache].append(car)
    
    # Montrer quelques exemples de collisions
    collisions_exemples = []
    for hache, chars in hachages_tous.items():
        if len(chars) > 1:
            collisions_exemples.append((hache, chars))
    
    if collisions_exemples:
        print(f"\nExemples de collisions dans tous les caractères ASCII :")
        for hache, chars in collisions_exemples[:3]:  # Montrer max 3 exemples
            print(f"Valeur hachée {hache:3d} (0x{hache:02X}) : {', '.join(f'\'{c}\'' for c in chars[:5])}")
            if len(chars) > 5:
                print(f"  ... et {len(chars) - 5} autres caractères")
    
    # Maintenant la recherche dans les caractères valides seulement
    caracteres = []
    for code in range(32, 127):  # Caractères ASCII imprimables
        car = chr(code)
        if is_valid_character(car):
            caracteres.append(car)
    
    print(f"\nNombre de caractères valides (TP3) : {len(caracteres)}")
    
    # Créer un dictionnaire valeur_hachee -> liste de caractères
    hachages = {}
    for car in caracteres:
        # H(car) = encodage UTF-8 (valeur numérique du premier octet)
        hache = car.encode('utf-8')[0]
        if hache not in hachages:
            hachages[hache] = []
        hachages[hache].append(car)
    
    # Chercher les collisions
    collisions_trouvees = []
    for hache, chars in hachages.items():
        if len(chars) > 1:
            collisions_trouvees.append((hache, chars))
    
    if collisions_trouvees:
        print(f"\nCollisions trouvées dans les caractères valides : {len(collisions_trouvees)}")
        total_paires = 0
        for hache, chars in collisions_trouvees:
            if len(chars) > 1:
                print(f"\nValeur hachée {hache:3d} (0x{hache:02X}) : {', '.join(f'\'{c}\'' for c in chars)}")
                # Afficher toutes les paires possibles
                for i in range(len(chars)):
                    for j in range(i + 1, len(chars)):
                        print(f"  '{chars[i]}' et '{chars[j]}' produisent la même valeur hachée")
                        total_paires += 1
        print(f"\nTotal des paires de collision : {total_paires}")
    else:
        print("\nAucune collision trouvée dans les caractères valides du TP3.")
        print("Chaque valeur de hachage correspond à au plus un caractère valide.")
        print("Cela montre que la fonction de hachage H(car) est injective sur l'ensemble")
        print("des caractères autorisés (lettres + caractères spéciaux sélectionnés).")
    
    # Montrer quelques exemples de collisions en utilisant des caractères Unicode
    print(f"\nExemples de collisions avec des caractères Unicode :")
    
    # Exemples de caractères qui ont le même premier octet UTF-8
    exemples_collisions = [
        (195, ['Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ']),  # Premier octet 195 (0xC3)
        (197, ['É', 'Ê', 'Ë']),  # Premier octet 197 (0xC5)
        (196, ['à', 'á', 'â', 'ã', 'ä', 'å']),  # Premier octet 196 (0xC4)
    ]
    
    for hache, chars in exemples_collisions:
        chars_filtres = [c for c in chars if ord(c) < 256]  # Garder seulement les caractères simples
        if len(chars_filtres) > 1:
            print(f"Valeur hachée {hache:3d} (0x{hache:02X}) : {', '.join(f'\'{c}\'' for c in chars_filtres[:4])}")
            if len(chars_filtres) > 4:
                print(f"  ... et {len(chars_filtres) - 4} autres caractères")


def exercice_3_preimages() -> None:
    """
    Exercice 3 : Recherche de préimages
    Pour une valeur h donnée, trouve un caractère qui donne cette valeur
    """
    print("\n" + "-"*80)
    print("EXERCICE 3 : RECHERCHE DE PRÉIMAGES")
    print("-"*80)
    
    # Choisir aléatoirement un caractère comme cible
    import random
    caracteres = []
    for code in range(32, 127):
        car = chr(code)
        if is_valid_character(car):
            caracteres.append(car)
    
    if not caracteres:
        print("Erreur : Aucun caractère valide trouvé.")
        return
    
    # Sélectionner un caractère cible aléatoirement
    cible = random.choice(caracteres)
    valeur_cible = cible.encode('utf-8')[0]
    
    print(f"Caractère cible choisi aléatoirement : '{cible}'")
    print(f"Valeur hachée cible : {valeur_cible} (0x{valeur_cible:02X})")
    print("\nRecherche d'une préimage pour cette valeur...")
    
    # Chercher une préimage (qui peut être le même caractère ou un autre)
    essais = 0
    trouve = False
    preimage = None
    
    while not trouve and essais < 1000:  # Limite de sécurité
        candidat = random.choice(caracteres)
        valeur_candidat = candidat.encode('utf-8')[0]
        essais += 1
        
        if valeur_candidat == valeur_cible:
            preimage = candidat
            trouve = True
    
    if trouve:
        print(f"Préimage trouvée après {essais} essais : '{preimage}'")
        if preimage == cible:
            print("(La préimage trouvée est le même caractère que la cible)")
        else:
            print("(Collision trouvée !)")
    else:
        print(f"Aucune préimage trouvée après {essais} essais.")
    
    # Calcul théorique
    print(f"\nProbabilité théorique de trouver une préimage : {1/len(caracteres):.4f}")
    print(f"(1 sur {len(caracteres)} caractères valides)")
    
    # Test avec plusieurs répétitions
    print("\nTest avec 10 répétitions :")
    essais_moyens = []
    for i in range(10):
        cible_test = random.choice(caracteres)
        valeur_test = cible_test.encode('utf-8')[0]
        
        essais_test = 0
        while True:
            candidat_test = random.choice(caracteres)
            valeur_candidat_test = candidat_test.encode('utf-8')[0]
            essais_test += 1
            
            if valeur_candidat_test == valeur_test:
                essais_moyens.append(essais_test)
                break
    
    moyenne = sum(essais_moyens) / len(essais_moyens)
    print(f"Nombre moyen d'essais : {moyenne:.1f}")
    print(f"(Théorique attendu : {len(caracteres)})")


def exercice_4_hachage_texte() -> None:
    """
    Exercice 4 : Fonction de hachage H* pour du texte
    H*(texte) = H(car1) ⊕ H(car2) ⊕ ... ⊕ H(carn)
    """
    print("\n" + "-"*80)
    print("EXERCICE 4 : FONCTION DE HACHAGE H*")
    print("-"*80)
    print("H*(texte) = H(car1) ⊕ H(car2) ⊕ ... ⊕ H(carn)")
    print("où ⊕ représente le XOR bit à bit")
    print("Le texte doit contenir uniquement : majuscules, minuscules et caractères spéciaux (!, #, (, ), *, +, /, ?)")
    
    texte = input("\nEntrez un texte : ").strip()
    
    if not texte:
        print("Erreur : Le texte ne peut pas être vide.")
        return
    
    # S'assurer que texte est une string
    if not isinstance(texte, str):
        print("Erreur : Le texte doit être une chaîne de caractères.")
        return
    
    # Vérification préalable que tous les caractères sont valides
    caracteres_invalides = []
    for car in texte:
        if not is_valid_character(car):
            caracteres_invalides.append(car)
    
    if caracteres_invalides:
        invalides_liste = []
        for c in caracteres_invalides:
            invalides_liste.append(f"'{c}'")
        invalides_str = ", ".join(invalides_liste)
        print(f"Erreur : Le texte contient des caractères non autorisés : {invalides_str}")
        print("Caractères autorisés : lettres (a-z, A-Z) et caractères spéciaux (!, #, (, ), *, +, /, ?)")
        return
    
    print(f"\nTexte validé : '{texte}'")
    print(f"Longueur : {len(texte)} caractères")
    
    # Calculer H* (XOR de tous les H(car))
    h_star = 0  # Valeur initiale pour le XOR
    
    print("\nCalcul détaillé :")
    print("Car | H(Car) | H*(courant)")
    print("-" * 30)
    
    for i, car in enumerate(texte):
        h_car = car.encode('utf-8')[0]  # H(car) - valeur numérique de l'octet UTF-8
        h_star ^= h_car  # XOR cumulatif
        
        print(f"'{car}' | {h_car:3d} (0x{h_car:02X}) | {h_star:3d} (0x{h_star:02X})")
    
    print("-" * 30)
    print(f"H*('{texte}') = {h_star} (0x{h_star:02X})")
    print(f"En binaire : {h_star:08b}")
    
    # Comparaison avec un autre texte
    print("\nComparaison avec un autre texte :")
    texte2 = input("Entrez un deuxième texte : ").strip()
    
    if texte2:
        # Vérification du deuxième texte
        caracteres_invalides2 = []
        for car in texte2:
            if not is_valid_character(car):
                caracteres_invalides2.append(car)
        
        if caracteres_invalides2:
            print(f'Erreur : Le deuxième texte contient des caractères non autorisés : {", ".join(f"\'{c}\'" for c in caracteres_invalides2)}')
            return
        
        h_star2 = 0
        for car in texte2:
            h_car = car.encode('utf-8')[0]
            h_star2 ^= h_car
        
        print(f"H*('{texte}')  = {h_star} (0x{h_star:02X})")
        print(f"H*('{texte2}') = {h_star2} (0x{h_star2:02X})")
        
        if h_star == h_star2:
            print("COLLISION ! Les deux textes donnent le même hachage.")
        else:
            print("Pas de collision.")


def exercice_5_attaque_dictionnaire() -> None:
    """
    Exercice 5 : Attaque sur le dictionnaire
    Utilise le fichier texte pour trouver des collisions
    """
    print("\n" + "-"*80)
    print("EXERCICE 5 : ATTAQUE SUR LE DICTIONNAIRE")
    print("-"*80)
    print("Utilisation du fichier texte pour trouver des collisions...")
    
    try:
        # Lire le fichier et extraire les mots valides
        mots = read_valid_characters_from_file(FICHIER_TEXTE)
        print(f"Fichier chargé : {len(mots)} mots valides trouvés")
        
        # Créer un dictionnaire hachage -> liste de mots
        hachages_mots = {}
        
        print("\nCalcul des hachages pour tous les mots...")
        for mot in mots:
            # Pour chaque mot, calculer H*(mot) = XOR de tous les H(car)
            hachage = 0
            for car in mot:
                if is_valid_character(car):
                    hachage ^= car.encode('utf-8')[0]  # H(car)
                else:
                    break  # Mot invalide
            else:
                # Mot valide, l'ajouter au dictionnaire
                if hachage not in hachages_mots:
                    hachages_mots[hachage] = []
                hachages_mots[hachage].append(mot)
        
        # Chercher les collisions
        collisions = []
        for hachage, liste_mots in hachages_mots.items():
            if len(liste_mots) > 1:
                collisions.append((hachage, liste_mots))
        
        print(f"\nCollisions trouvées : {len(collisions)}")
        
        if collisions:
            print("\nExemples de collisions :")
            for i, (hachage, mots_collision) in enumerate(collisions[:10]):  # Max 10
                mots_str = ", ".join(f"'{mot}'" for mot in mots_collision[:5])
                print(f"{i+1}. Valeur {hachage:3d} (0x{hachage:02X}) : {mots_str}")
        else:
            print("Aucune collision trouvée dans le dictionnaire.")
        
        # Statistiques
        total_mots = sum(len(mots) for mots in hachages_mots.values())
        valeurs_uniques = len(hachages_mots)
        print(f"\nStatistiques :")
        print(f"- Mots traités : {total_mots}")
        print(f"- Valeurs de hachage uniques : {valeurs_uniques}")
        print(f"- Taux de collision : {(total_mots - valeurs_uniques) / total_mots * 100:.2f}%")
        
        # Recherche d'une préimage spécifique
        print("\nRecherche d'une préimage pour une valeur spécifique :")
        try:
            valeur_cible = int(input("Entrez une valeur de hachage (0-255) : "))
            if 0 <= valeur_cible <= 255:
                if valeur_cible in hachages_mots:
                    mots_trouves = hachages_mots[valeur_cible]
                    mots_str = ", ".join(f"'{mot}'" for mot in mots_trouves[:10])
                    print(f"Préimages trouvées pour {valeur_cible} : {mots_str}")
                    if len(mots_trouves) > 10:
                        print(f"... et {len(mots_trouves) - 10} autres")
                else:
                    print(f"Aucune préimage trouvée pour la valeur {valeur_cible}")
            else:
                print("Valeur hors limites (0-255)")
        except ValueError:
            print("Valeur invalide")
            
    except (FileNotFoundError, IOError) as e:
        print(f"Erreur : {e}")


if __name__ == "__main__":
    menu_principal()
