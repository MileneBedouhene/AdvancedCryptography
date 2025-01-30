import random
import string

def generate_substitution_table():
    letters = list(string.ascii_lowercase)
    shuffled_letters = letters[:]
    random.shuffle(shuffled_letters)
    return dict(zip(letters, shuffled_letters))

def encrypt(text, substitution_table):
    return ''.join(substitution_table.get(char, char) for char in text.lower())

def decrypt(encrypted_text, substitution_table):
    reversed_table = {v: k for k, v in substitution_table.items()}
    return ''.join(reversed_table.get(char, char) for char in encrypted_text)

while True:
    print("-" * 50)
    print("1. Chiffrer un texte.")
    print("2. Déchiffrer un texte.")
    print("3. Quitter.")
    print("-" * 50)

    try:
        choix = int(input("Veuillez choisir une option : "))
    except ValueError:
        print("-" * 50)
        print("Veuillez entrer un nombre valide.")
        print("-" * 50)
        continue

    if choix == 1:
        text = input("Entrez le texte à chiffrer : ")
        substitution_table = generate_substitution_table()
        crypted_text = encrypt(text, substitution_table)
        print("-" * 50)
        print(f"Texte chiffré : {crypted_text}")
        print("Table de substitution :", substitution_table)
        print("-" * 50)
    
    elif choix == 2:
        text = input("Entrez le texte à déchiffrer : ")
        try:
            substitution_table = eval(input("Entrez la table de substitution utilisée : "))
            decrypted_text = decrypt(text, substitution_table)
            print("-" * 50)
            print(f"Texte déchiffré : {decrypted_text}")
            print("-" * 50)
        except Exception as e:
            print("-" * 50)
            print(f"Erreur : {e}")
            print("-" * 50)
    
    elif choix == 3:
        print("-" * 50)
        print("Au revoir!")
        print("-" * 50)
        break
    
    else:
        print("-" * 50)
        print("Option invalide. Veuillez choisir entre 1, 2 ou 3.")
        print("-" * 50)
