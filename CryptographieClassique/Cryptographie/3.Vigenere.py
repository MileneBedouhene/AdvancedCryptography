# GENERATION DE LA TABLE DE VIGENERE
def table_vigenere():
    table = []
    for i in range(26):
        row = []
        for j in range(26):
            row.append(chr((i + j) % 26 + ord('A')))
        table.append(row)
    return table


# EXTRACTION DE LA CLE DE CHIFFREMENT
def ckey(message, key):
    key = key.upper()
    ckey = key
    while len(ckey) < len(message):
        ckey += key
    return ckey[:len(message)]


# CHIFFREMENT
def vigenere_chiffre(message, key):
    key = ckey(message, key)
    table = table_vigenere()
    cipher_text = []
    
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            row = ord(key[i]) - ord('A')
            if char.isupper():
                col = ord(char) - ord('A')
                cipher_text.append(table[row][col])
            else:
                col = ord(char) - ord('a')
                cipher_text.append(table[row][col].lower())
        else:
            cipher_text.append(char)
    
    return ''.join(cipher_text)


# DECHIFFREMENT
def vigenere_dechiffre(cipher_text, key):
    key = ckey(cipher_text, key)
    table = table_vigenere()
    message = []
    
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if char.isalpha():
            row = ord(key[i]) - ord('A')
            if char.isupper():
                col = table[row].index(char)
                message.append(chr(col + ord('A')))
            else:
                col = table[row].index(char.upper())
                message.append(chr(col + ord('a')))
        else:
            message.append(char)
    
    return ''.join(message)


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
    clef = input("Entrez la clé de chiffrement (mot) : ")
    print("-" * 50)
    resultat = vigenere_chiffre(texte, clef)
    print("-" * 50)
    print(f"Texte chiffré : {resultat}")
    print("-" * 50)
    
elif choix == 2:
    print("-" * 50)
    texte = input("Entrez le texte à déchiffrer : ")
    print("-" * 50)
    clef = input("Entrez la clé de déchiffrement (mot) : ")
    print("-" * 50)
    resultat = vigenere_dechiffre(texte, clef)
    print("-" * 50)
    print(f"Texte déchiffré : {resultat}")
    print("-" * 50)
    
elif choix == 3:
    print("-" * 50)
    print("Au revoir!")
    print("-" * 50)
