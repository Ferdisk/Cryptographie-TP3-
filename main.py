from collision_preimages import trouver_toutes_les_collisions, trouver_preimage_aleatoire
from hachage_xor import H_star
from attaques_cibles import trouver_collisions_dictionnaire

def saisir_caractere():
    car = input("Veuillez entrer un unique caractère : ")
    while len(car) != 1 or (not car.isalnum() and car not in ['!', '#', '(', ')', '*', '+', '/', '?']):
        car = input("Veuillez entrer un unique caractère alphanumérique ou un des caractères spéciaux suivants (! # ( ) * + / ?) : ")
    print(f"Le caractère {car.encode('utf-8').hex()} est valide.")
    return car

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Saisir et valider un caractère")
        print("2 - Recherche de collision")
        print("3 - Recherche de préimage")
        print("4 - Calculer H*(texte)")
        print("5 - Trouver collisions à partir d’un dictionnaire")
        print("0 - Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            saisir_caractere()
        elif choix == "2":
            print("\n=== Recherche de collision ===")
            trouver_toutes_les_collisions()
        elif choix == "3":
            print("\n=== Recherche de préimage ===")
            trouver_preimage_aleatoire() 
        elif choix == "4":
            texte = input("\nEntrez un texte : ")
            print(f"H*(\"{texte}\") = {H_star(texte)}")
        elif choix == "5":
            trouver_collisions_dictionnaire("dictionnaire.txt")
        elif choix == "0":
            print("Au revoir ! 👋")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    menu()
