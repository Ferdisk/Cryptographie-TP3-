from hachage_xor import H_star


def trouver_collisions_dictionnaire(fichier_dico: str):
    """Cherche des collisions H* entre mots du dictionnaire"""
    with open(fichier_dico, "r", encoding="utf-8") as f:
        mots = [m.strip() for m in f.readlines() if m.strip()]

    hachages = {}
    essais = 0

    for mot in mots:
        essais += 1
        h = H_star(mot)
        if h in hachages:
            print(f"Collision trouvée après {essais} essais : '{hachages[h]}' et '{mot}' donnent {h}")
            return
        hachages[h] = mot

    print("Aucune collision trouvée dans le dictionnaire.")

