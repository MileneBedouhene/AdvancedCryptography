import numpy as np

def texte_en_nombres(texte):
    return [ord(char) - ord('A') for char in texte.upper() if 'A' <= char <= 'Z']

def nombres_en_texte(nombres):
    return ''.join(chr(num + ord('A')) for num in nombres)

def chiffrer_hill(texte, cle):
    n = len(cle)
    texte_nombres = texte_en_nombres(texte)
    
    # Compléter le texte si nécessaire pour correspondre à la taille de la matrice
    while len(texte_nombres) % n != 0:
        texte_nombres.append(0)  # Ajouter 'A' (0) en padding
    
    texte_chiffre = []
    for i in range(0, len(texte_nombres), n):
        bloc = np.array(texte_nombres[i:i+n]).reshape(n, 1)
        bloc_chiffre = np.dot(cle, bloc) % 26
        texte_chiffre.extend(bloc_chiffre.flatten())
    
    return nombres_en_texte(texte_chiffre)

def dechiffrer_hill(texte, cle):
    n = len(cle)
    texte_nombres = texte_en_nombres(texte)
    
    # Calculer l'inverse de la matrice clé modulo 26
    det = int(round(np.linalg.det(cle)))
    det_inv = pow(det, -1, 26)  # Inverse modulaire du déterminant
    
    cle_inv = (det_inv * np.round(det * np.linalg.inv(cle)).astype(int)) % 26
    
    texte_dechiffre = []
    for i in range(0, len(texte_nombres), n):
        bloc = np.array(texte_nombres[i:i+n]).reshape(n, 1)
        bloc_dechiffre = np.dot(cle_inv, bloc) % 26
        texte_dechiffre.extend(bloc_dechiffre.flatten())
    
    # Suppression du padding ('A' ajouté)
    while texte_dechiffre and texte_dechiffre[-1] == 0:
        texte_dechiffre.pop()
    
    return nombres_en_texte(texte_dechiffre)


# Exemple d'utilisation
cle = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # Matrice clé 3x3
message = "Milene"
message_chiffre = chiffrer_hill(message, cle)
message_dechiffre = dechiffrer_hill(message_chiffre, cle)

print(f"Message chiffré: {message_chiffre}")
print(f"Message déchiffré: {message_dechiffre}")

