import string

# Génère la matrice de chiffrement Playfair en fonction de la clé fournie
def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")  # Remplace 'J' par 'I' pour respecter la règle de Playfair
    alphabet = string.ascii_uppercase.replace("J", "")  # Alphabet sans 'J'
    matrix = []
    used_chars = set()
    
    # Ajouter la clé à la matrice
    for char in key:
        if char not in used_chars and char in alphabet:
            matrix.append(char)
            used_chars.add(char)
    
    # Ajouter le reste de l'alphabet
    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

# Formate le message en supprimant les caractères non alphabétiques, 
# en remplaçant 'J' par 'I' et en s'assurant que les paires sont valides
def format_message(message):
    message = ''.join([c.upper().replace("J", "I") for c in message if c.isalpha()])
    formatted = ""
    i = 0
    while i < len(message):
        char1 = message[i]
        char2 = message[i+1] if i+1 < len(message) else 'X'
        
        if char1 == char2:
            formatted += char1 + 'X'
            i += 1
        else:
            formatted += char1 + char2
            i += 2
    
    return formatted

# Trouve la position d'un caractère dans la matrice Playfair
def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    raise ValueError(f"Le caractère {char} n'est pas trouvé dans la matrice.")

# Chiffre un message en utilisant le chiffrement Playfair
def playfair_encrypt(message, key):
    matrix = generate_playfair_matrix(key)
    message = format_message(message)
    cipher_text = ""
    print(matrix)
    
    for i in range(0, len(message), 2):
        char1, char2 = message[i], message[i+1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        
        if row1 == row2:  # Même ligne
            cipher_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Même colonne
            cipher_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    
    return cipher_text

# Déchiffre un message en utilisant le chiffrement Playfair
def playfair_decrypt(cipher_text, key):
    matrix = generate_playfair_matrix(key)
    message = ""
    print(matrix)
    
    for i in range(0, len(cipher_text), 2):
        char1, char2 = cipher_text[i], cipher_text[i+1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        
        if row1 == row2:  # Même ligne
            message += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Même colonne
            message += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle
            message += matrix[row1][col2] + matrix[row2][col1]
    
    return message

# Menu principal

print("-" * 50)
print("1. Chiffrer un texte avec Playfair.")
print("2. Déchiffrer un texte avec Playfair.")
print("3. Quitter.")
print("-" * 50)
    

choix = int(input("Veuillez choisir une option : "))

if choix == 1:
    texte = input("Entrez le texte à chiffrer : ")
    clef = input("Entrez la clé de chiffrement : ")
    resultat = playfair_encrypt(texte, clef)
    print(f"Texte chiffré : {resultat}")
    
elif choix == 2:
    texte = input("Entrez le texte à déchiffrer : ")
    clef = input("Entrez la clé de déchiffrement : ")
    resultat = playfair_decrypt(texte, clef)
    print(f"Texte déchiffré : {resultat}")
    
elif choix == 3:
        print("Au revoir!")
        
    
