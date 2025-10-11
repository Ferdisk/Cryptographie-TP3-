
from collision_preimages import trouver_collision, trouver_preimage
from hachage_xor import H_star
from attaques_cibles import trouver_collisions_dictionnaire


if __name__ == "__main__":

    car: str = input("Veuillez enterer un unique caractère : ")
    
    while len(car) != 1 or (not car.isalnum() and car not in ['!', '#', '(', ')','*','+','/','?']):
        car = input("Veuillez enterer un unique caractère alphanumérique ou un des caractères spéciaux suivants ! # ( ) * + / ? : ")
    
    print(f"Le caractère {car.encode('utf-8').hex()} est valide.")

    print("=== Recherche de collision ===")
    trouver_collision()

    print("\n=== Recherche de préimage ===")
    trouver_preimage()

    texte = input("\nEntrez un texte : ")
    print(f"H*(\"{texte}\") = {H_star(texte)}")
    trouver_collisions_dictionnaire("dictionnaire.txt")