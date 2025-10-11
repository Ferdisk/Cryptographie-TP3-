# TP3 - Hachage Cryptographique et Encodage UTF-8

## Description

Ce projet implémente un programme de hachage cryptographique et d'encodage UTF-8 dans le cadre du TP3 de Cryptographie.

### Fonctionnalités principales

1. **Lecture de fichier texte** : Extraction des caractères valides depuis le fichier `ods5.txt`

2. **Validation de caractère** : Les caractères acceptés sont :
   - Les lettres (majuscules et minuscules : a-z, A-Z), OU
   - Les caractères spéciaux : `!`, `#`, `(`, `)`, `*`, `+`, `/`, `?`
   - **Note** : Les chiffres (0-9) ne sont PAS acceptés

3. **Encodage UTF-8** : Affiche la représentation du caractère en octets UTF-8

4. **Fonctions de hachage** : Calcule et affiche les hash cryptographiques avec plusieurs algorithmes (MD5, SHA-1, SHA-256, SHA-512, BLAKE2b)

## Architecture du Projet

```
Cryptographie-TP3-/
├── src/
│   ├── __init__.py
│   ├── hash/
│   │   ├── __init__.py
│   │   ├── hash_functions.py    # Fonctions de hachage cryptographique
│   │   └── encoding.py          # Gestion de l'encodage UTF-8
│   ├── utils/
│   │   ├── __init__.py
│   │   └── input_validator.py   # Validation des entrées utilisateur
│   └── main.py                  # Point d'entrée principal
├── H.py                         # Fichier original (conservé)
├── README.md
└── RAPPORT.md
```

## Installation et Utilisation

### Prérequis

- Python 3.8 ou supérieur
- Aucune dépendance externe (utilise uniquement la bibliothèque standard Python)

### Exécution du Programme

```bash
python src/main.py
```

Le menu principal propose 5 options :

1. **Afficher les caractères du fichier texte** : Liste tous les caractères valides trouvés dans `ods5.txt`
2. **Afficher l'encodage UTF-8 d'un caractère du fichier** : Affiche les octets UTF-8 d'un caractère
3. **Calculer les hash d'un caractère** : Affiche tous les hash cryptographiques
4. **Comparer les hash de deux caractères** : Démontre l'effet avalanche
5. **Mode interactif complet** : Affiche encodage ET hash

## Menu Principal

Le programme propose les 5 exercices demandés dans le TP3 :

```
1. Exercice 1 : Fonction de hachage H
2. Exercice 2 : Recherche de collisions
3. Exercice 3 : Recherche de préimages
4. Exercice 4 : Fonction de hachage H* pour texte
5. Exercice 5 : Attaque sur le dictionnaire
0. Quitter
```

### Exercice 1 : Fonction de hachage H

Saisissez un caractère (lettre ou caractère spécial autorisé) pour voir son encodage UTF-8.

**Caractères acceptés** : lettres (a-z, A-Z) et caractères spéciaux (!, #, (, ), *, +, /, ?)

**Fonction H** : H(car) = encodage UTF-8 du caractère (valeur entre 33 et 122)

**Exemple** :
```
Caractère : A
Encodage UTF-8 : 65 (0x41)
Binaire : 01000001
```

### Exercice 2 : Recherche de collisions

Recherche automatique de collisions dans la fonction de hachage H.

**Résultat** : Aucune collision trouvée (fonction parfaite pour ces caractères).

### Exercice 3 : Recherche de préimages

Recherche d'un caractère qui donne une valeur de hachage spécifique.

**Méthode** : Recherche aléatoire avec calcul de probabilités.

### Exercice 4 : Fonction de hachage H* pour texte

Calcule H*(texte) = H(car1) ⊕ H(car2) ⊕ ... ⊕ H(carn)

**Exemple** :
```
Texte : "AB"
H*(AB) = H(A) ⊕ H(B) = 65 ⊕ 66 = 3
```

### Exercice 5 : Attaque sur le dictionnaire

Utilise le fichier `ods5.txt` pour trouver des collisions parmi les mots du dictionnaire.

**Méthode** : Calcul de H*(mot) pour chaque mot, recherche de collisions.

## Modules Disponibles

### 1. `src.utils.file_reader`

Lecture et extraction de caractères depuis un fichier texte :

```python
from src.utils.file_reader import read_valid_characters_from_file

# Lire les caractères valides du fichier
chars = read_valid_characters_from_file('ods5.txt')
print(f"Nombre de caractères : {len(chars)}")
```

### 2. `src.hash.encoding`

Fonctions d'encodage UTF-8 :

```python
from src.hash.encoding import char_to_utf8_decimal, display_encoding_info

# Obtenir les octets en décimal
octets = char_to_utf8_decimal('A')  # [65]

# Afficher l'encodage
display_encoding_info('é')  # [195, 169]
```

### 3. `src.hash.hash_functions`

Fonctions de hachage cryptographique :

```python
from src.hash.hash_functions import hash_sha256, display_all_hashes

# Calculer un hash SHA-256
hash_value = hash_sha256('Hello')

# Afficher tous les hash
display_all_hashes('A')

# Comparer les hash de deux chaînes
compare_hashes('A', 'B')
```

### 4. `src.utils.input_validator`

Validation des entrées utilisateur :

```python
from src.utils.input_validator import validate_character, is_valid_character

# Valider un caractère manuellement
if is_valid_character('A'):
    print("Caractere valide")

# Demander un caractère à l'utilisateur avec validation
car = validate_character()
```

## Algorithmes de Hachage Disponibles

| Algorithme | Taille du hash | Sécurité | Note |
|------------|----------------|----------|------|
| **MD5** | 128 bits (32 hex) | Cassé | Usage pédagogique uniquement |
| **SHA-1** | 160 bits (40 hex) | Vulnérable | Déprécié depuis 2017 |
| **SHA-256** | 256 bits (64 hex) | Sécurisé | Recommandé |
| **SHA-512** | 512 bits (128 hex) | Très sécurisé | Haute sécurité |
| **BLAKE2b** | 512 bits (128 hex) | Très sécurisé | Rapide et moderne |

## Exemples d'Utilisation

### Exemple 1 : Afficher l'encodage UTF-8

```python
from src.hash.encoding import display_encoding_info

display_encoding_info('A')
# Sortie :
# Caractere : 'A'
# Octets UTF-8 : [65]

display_encoding_info('é')
# Sortie :
# Caractere : 'é'
# Octets UTF-8 : [195, 169]
```

### Exemple 2 : Calculer des Hash

```python
from src.hash.hash_functions import hash_all

hashes = hash_all('Hello')
print(hashes['sha256'])
# Sortie : 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
```

### Exemple 3 : Comparer l'Effet Avalanche

```python
from src.hash.hash_functions import compare_hashes

compare_hashes('A', 'B')
# Affiche une comparaison complète des hash
```

## Concepts Cryptographiques

### 1. Encodage UTF-8
- Représentation multi-octets des caractères
- Compatibilité ASCII pour les caractères de base (0-127)
- Support des caractères internationaux (2 octets ou plus)

### 2. Fonctions de Hachage
- **Déterminisme** : même entrée → même hash
- **Effet avalanche** : petit changement → hash complètement différent
- **Fonction à sens unique** : impossible de retrouver l'entrée à partir du hash
- **Résistance aux collisions** : difficile de trouver deux entrées avec le même hash

## Principes Appliqués

- Programmation modulaire : séparation claire des responsabilités
- Documentation complète : docstrings et commentaires
- Type hints : annotations de types pour la clarté
- Architecture propre : organisation logique des fichiers

## Auteur

Projet pédagogique - BUT Informatique  
Date : Octobre 2025