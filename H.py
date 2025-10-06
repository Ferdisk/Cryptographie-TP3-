
if __name__ == "__main__":

    car: str = input("Veuillez enterer un unique caractère : ")
    
    while len(car) != 1 or (not car.isalnum() and car not in ['!', '#', '(', ')','*','+','/','?']):
        car = input("Veuillez enterer un unique caractère alphanumérique ou un des caractères spéciaux suivants ! # ( ) * + / ? : ")
    
    print(f"Le caractère {car.encode('utf-8').hex()} est valide.")

    
