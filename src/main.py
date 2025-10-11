"""
Programme principal du TP3 - Hachage Cryptographique

Ce programme démontre l'utilisation des fonctions de hachage cryptographique
et de l'encodage UTF-8 sur des caractères issus d'un fichier texte.
"""

import sys
from pathlib import Path

# Ajouter le répertoire parent au PYTHONPATH pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from menu import menu_principal


if __name__ == "__main__":
    menu_principal()
