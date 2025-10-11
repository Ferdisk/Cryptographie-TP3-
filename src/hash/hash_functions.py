"""
Module de fonctions de hachage cryptographique

Ce module fournit des fonctions pour calculer différents hash cryptographiques
(MD5, SHA-1, SHA-256, SHA-512, BLAKE2) sur des chaînes de caractères.
"""

import hashlib
from typing import Dict


def hash_md5(data: str) -> str:
    """
    Calcule le hash MD5 d'une chaîne de caractères.
    
    Attention : MD5 est considéré comme cryptographiquement cassé.
    À utiliser uniquement pour des besoins pédagogiques ou de compatibilité.
    
    Args:
        data (str): La chaîne à hasher
    
    Returns:
        str: Le hash MD5 en hexadécimal (32 caractères)
    
    Examples:
        >>> hash_md5('A')
        '7fc56270e7a70fa81a5935b72eacbe29'
        >>> hash_md5('Hello')
        '8b1a9953c4611296a827abf8c47804d7'
    """
    return hashlib.md5(data.encode('utf-8')).hexdigest()


def hash_sha1(data: str) -> str:
    """
    Calcule le hash SHA-1 d'une chaîne de caractères.
    
    Attention : SHA-1 est considéré comme vulnérable depuis 2017.
    À utiliser avec précaution.
    
    Args:
        data (str): La chaîne à hasher
    
    Returns:
        str: Le hash SHA-1 en hexadécimal (40 caractères)
    
    Examples:
        >>> hash_sha1('A')
        '6dcd4ce23d88e2ee9568ba546c007c63d9131c1b'
    """
    return hashlib.sha1(data.encode('utf-8')).hexdigest()


def hash_sha256(data: str) -> str:
    """
    Calcule le hash SHA-256 d'une chaîne de caractères.
    
    SHA-256 fait partie de la famille SHA-2 et est actuellement considéré
    comme sécurisé pour la plupart des applications cryptographiques.
    
    Args:
        data (str): La chaîne à hasher
    
    Returns:
        str: Le hash SHA-256 en hexadécimal (64 caractères)
    
    Examples:
        >>> hash_sha256('A')
        '559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd'
    """
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def hash_sha512(data: str) -> str:
    """
    Calcule le hash SHA-512 d'une chaîne de caractères.
    
    SHA-512 offre un niveau de sécurité plus élevé que SHA-256
    au prix d'un hash plus long.
    
    Args:
        data (str): La chaîne à hasher
    
    Returns:
        str: Le hash SHA-512 en hexadécimal (128 caractères)
    
    Examples:
        >>> hash_sha512('A')
        '21b4f4bd9e64ed355c3eb676a28ebedaf6d8f17bdc365995b319097153044080516bd083bfcce66121a3072646994c8430cc382b8dc543e84880183bf856cff5'
    """
    return hashlib.sha512(data.encode('utf-8')).hexdigest()


def hash_blake2b(data: str, digest_size: int = 64) -> str:
    """
    Calcule le hash BLAKE2b d'une chaîne de caractères.
    
    BLAKE2b est plus rapide que MD5, SHA-1, SHA-2, et SHA-3,
    tout en étant au moins aussi sécurisé que SHA-3.
    
    Args:
        data (str): La chaîne à hasher
        digest_size (int): Taille du digest en bytes (1-64, par défaut 64)
    
    Returns:
        str: Le hash BLAKE2b en hexadécimal
    
    Examples:
        >>> hash_blake2b('A')
        '4a0d23e97632d3cc222a559bced0e0ef0a13c8d8e0c4c96f2f7b5c0f66d5e20b333b0c30f0faad02e0e7e32c80e4a8cd17b9f5f1f5e8b5b3f3e0f4c2a0b7e5f1'
    """
    return hashlib.blake2b(data.encode('utf-8'), digest_size=digest_size).hexdigest()


def hash_all(data: str) -> Dict[str, str]:
    """
    Calcule tous les hash disponibles pour une chaîne donnée.
    
    Args:
        data (str): La chaîne à hasher
    
    Returns:
        Dict[str, str]: Dictionnaire avec tous les hash calculés
                       {algorithme: hash_hexadecimal}
    
    Examples:
        >>> hashes = hash_all('A')
        >>> print(hashes['sha256'])
        '559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd'
    """
    return {
        'md5': hash_md5(data),
        'sha1': hash_sha1(data),
        'sha256': hash_sha256(data),
        'sha512': hash_sha512(data),
        'blake2b': hash_blake2b(data)
    }


def compare_hashes(data1: str, data2: str) -> None:
    """
    Compare les hash de deux chaînes de caractères et affiche les résultats.
    
    Utile pour démontrer l'effet avalanche : un petit changement dans l'entrée
    produit un hash complètement différent.
    
    Args:
        data1 (str): Première chaîne
        data2 (str): Deuxième chaîne
    
    Examples:
        >>> compare_hashes('A', 'B')
        Comparaison des hash :
        Données 1 : 'A'
        Données 2 : 'B'
        ...
    """
    hashes1 = hash_all(data1)
    hashes2 = hash_all(data2)
    
    print(f"\n{'='*80}")
    print(f"Comparaison des hash")
    print(f"{'='*80}")
    print(f"Données 1 : '{data1}'")
    print(f"Données 2 : '{data2}'")
    print(f"{'='*80}\n")
    
    for algo in hashes1.keys():
        print(f"{algo.upper():>10} :")
        print(f"  Data 1 : {hashes1[algo]}")
        print(f"  Data 2 : {hashes2[algo]}")
        print(f"  Égaux  : {hashes1[algo] == hashes2[algo]}")
        print()


def display_all_hashes(data: str) -> None:
    """
    Affiche tous les hash d'une chaîne de manière formatée.
    
    Args:
        data (str): La chaîne à hasher
    
    Examples:
        >>> display_all_hashes('A')
        Hash pour : 'A'
        ========================================
        MD5      : 7fc56270e7a70fa81a5935b72eacbe29
        SHA-1    : 6dcd4ce23d88e2ee9568ba546c007c63d9131c1b
        ...
    """
    hashes = hash_all(data)
    
    print(f"\n{'='*80}")
    print(f"Hash pour : '{data}'")
    print(f"{'='*80}")
    
    for algo, hash_value in hashes.items():
        print(f"{algo.upper():>10} : {hash_value}")
    
    print(f"{'='*80}\n")
