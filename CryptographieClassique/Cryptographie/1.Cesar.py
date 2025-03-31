# Chiffrement

def cesar_chiffre_mixte(text, decalage):
    resultat = ""
    for char in text:
        if char.isupper():
            resultat += chr((ord(char) - 65 + decalage) % 26 + 65)
        elif char.islower():
            resultat += chr((ord(char) - 97 + decalage) % 26 + 97)
        else:
            resultat += char
    return resultat

# Dechiffrement
def cesar_dechiffre_mixte(text, decalage):
    resultat = ""
    for char in text:
        if char.isupper():
            resultat += chr((ord(char) - 65 - decalage) % 26 + 65)
        elif char.islower():
            resultat += chr((ord(char) - 97 - decalage) % 26 + 97)
        else:
            resultat += char
    return resultat

# Menu principal

print("-" * 50)
print("1. Chiffrer un texte.")
print("2. Déchiffrer un texte.")
print("3. Quitter.")
print("-" * 50)


print("-" * 50)
choix = int(input("Veuillez choisir une option : "))
print("-" * 50)



if choix == 1:
    print("-" * 50)
    texte = input("Entrez le texte à chiffrer : ")
    print("-" * 50)
    try:
        print("-" * 50)
        clef = int(input("Entrez la clé de chiffrement (un entier) : "))
        print("-" * 50)
        if clef < 0:
            print("-" * 50)
            raise ValueError("La clé doit être un entier positif."+"-" * 50)
            
        resultat = cesar_chiffre_mixte(texte, clef)
        print("-" * 50)
        print(f"Texte chiffré : {resultat}")
        print("-" * 50)
    except ValueError as e:
        print("-" * 50)
        print(f"Erreur : {e}")
        print("-" * 50)

elif choix == 2:
    texte = input("Entrez le texte à déchiffrer : ")
    print("-" * 50)
    try:
        clef = int(input("Entrez la clé de déchiffrement (un entier) : "))
        print("-" * 50)
        if clef < 0:
            raise ValueError("La clé doit être un entier positif.")
        resultat = cesar_dechiffre_mixte(texte, clef)
        print(f"Texte déchiffré : {resultat}")
        print("-" * 50)
    except ValueError as e:
        print("-" * 50)
        print(f"Erreur : {e}")
        print("-" * 50)

elif choix == 3:
    print("-" * 50)
    print("Au revoir!")
    print("-" * 50)
    


