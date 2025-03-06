import string
from math import gcd

def mod_inverse(a, m):
    """
    Calcule l'inverse modulaire de a modulo m.
    Renvoie l'inverse x tel que (a*x) % m == 1.
    Si a et m ne sont pas premiers entre eux, renvoie None.
    """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(plaintext, a, b):
    """
    Chiffre un texte en clair à l'aide du chiffre affine.
    La formule utilisée est : y = (a*x + b) mod 26.
    - plaintext : le texte en clair (lettres uniquement, peut être en majuscules ou minuscules)
    - a et b : clés du chiffrement. a doit être premier avec 26.
    """
    if gcd(a, 26) != 1:
        raise ValueError("La valeur de 'a' doit être premier avec 26.")
    
    plaintext = plaintext.upper()
    ciphertext = ""
    
    for char in plaintext:
        if char in string.ascii_uppercase:
            x = ord(char) - ord('A')
            y = (a * x + b) % 26
            ciphertext += chr(y + ord('A'))
        else:
            # On conserve les caractères non alphabétiques inchangés
            ciphertext += char
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    """
    Déchiffre un texte chiffré avec le chiffre affine.
    La formule utilisée est : x = a_inv * (y - b) mod 26,
    où a_inv est l'inverse modulaire de a modulo 26.
    """
    if gcd(a, 26) != 1:
        raise ValueError("La valeur de 'a' doit être premier avec 26.")
    
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("L'inverse modulaire n'a pas pu être calculé pour a.")
    
    ciphertext = ciphertext.upper()
    plaintext = ""
    
    for char in ciphertext:
        if char in string.ascii_uppercase:
            y = ord(char) - ord('A')
            x = (a_inv * (y - b)) % 26
            plaintext += chr(x + ord('A'))
        else:
            plaintext += char
    return plaintext

# Exemple d'utilisation
if __name__ == '__main__':
    texte = "AFFINE CIPHER EXAMPLE"
    a = 5  # doit être premier avec 26, par exemple : 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25
    b = 8

    print("Texte en clair :", texte)
    texte_chiffre = affine_encrypt(texte, a, b)
    print("Texte chiffré :", texte_chiffre)

    texte_dechiffre = affine_decrypt(texte_chiffre, a, b)
    print("Texte déchiffré :", texte_dechiffre)
