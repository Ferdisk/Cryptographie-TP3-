# TP3 - Hachage Cryptographique et Encodage UTF-8

## Description

Ce projet implémente un programme de hachage cryptographique simple et d'encodage UTF-8 dans le cadre du TP3 de Cryptographie.

### Fonctionnalités principales

1. **Lecture de fichier texte** : Extraction des caractères valides depuis le fichier `ods5.txt`

2. **Validation de caractère** : Les caractères acceptés sont :
   - Les lettres (majuscules et minuscules : a-z, A-Z), OU
   - Les caractères spéciaux : `!`, `#`, `(`, `)`, `*`, `+`, `/`, `?`
   - **Note** : Les chiffres (0-9) ne sont PAS acceptés

3. **Encodage UTF-8** : Affiche la représentation du caractère en octets UTF-8

4. **Fonction de hachage H** : H(car) = premier octet UTF-8 du caractère (valeur entre 33 et 122)

5. **Fonction de hachage H*** : H*(texte) = H(car1) ⊕ H(car2) ⊕ ... ⊕ H(carn)

## Architecture du Projet

```
Cryptographie-TP3-/
├── src/
│   ├── __init__.py
│   ├── exercises.py          # Tous les exercices du TP3
│   ├── menu.py               # Interface utilisateur et menu principal
│   ├── main.py               # Point d'entrée principal
│   ├── hash/
│   │   ├── __init__.py
│   │   └── encoding.py       # Gestion de l'encodage UTF-8
│   └── utils/
│       ├── __init__.py
│       ├── file_reader.py    # Lecture du fichier texte
│       └── input_validator.py # Validation des entrées utilisateur
├── ods5.txt                  # Fichier texte source
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

Le menu principal propose 4 exercices :

```text
TP3 - Cryptographie - Fonctions de Hachage
==================================================
1. Exercice 1 : Fonction de hachage H
2. Exercice 2 : Recherche de collisions et de préimages
3. Exercice 3 : Fonction de hachage H* pour texte
4. Exercice 4 : Attaque sur le dictionnaire
0. Quitter
```

## Exercices Implémentés

### Exercice 1 : Fonction de hachage H

Saisissez un caractère (lettre ou caractère spécial autorisé) pour voir son encodage UTF-8.

**Caractères acceptés** : lettres (a-z, A-Z) et caractères spéciaux (!, #, (, ), *, +, /, ?)

**Fonction H** : H(car) = premier octet UTF-8 du caractère (valeur entre 33 et 122)

**Exemple** :
```text
Caractère : 'A'
Octets UTF-8 : [65]
```

### Exercice 2 : Recherche de collisions et de préimages

**Recherche de collisions** : Recherche automatique de collisions dans la fonction de hachage H.

**Résultat** : Aucune collision trouvée parmi les caractères valides du TP3.

**Recherche de préimages** : Pour une valeur de hachage donnée, trouve un caractère qui donne cette valeur.

### Exercice 3 : Fonction de hachage H* pour texte

Calcule H*(texte) = H(car1) ⊕ H(car2) ⊕ ... ⊕ H(carn)

Où ⊕ représente le XOR bit à bit.

**Exemple** :

```text
Texte : "AB"
H*(AB) = H(A) ⊕ H(B) = 65 ⊕ 66 = 3
```

### Exercice 4 : Attaque sur le dictionnaire

Utilise le fichier `ods5.txt` pour trouver des collisions parmi les mots du dictionnaire.

**Méthode** : Calcul de H*(mot) pour chaque mot, recherche de collisions.