def ksa(key):
    """Initialisation de la permutation S-Box avec la clé"""
    S = list(range(256))  # Tableau S initialisé avec [0, 1, ..., 255]
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]  # Échange des valeurs
    return S

def prga(S, length):
    """Génération du flot de clés pseudo-aléatoires"""
    i = j = 0
    key_stream = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Échange des valeurs
        K = S[(S[i] + S[j]) % 256]
        key_stream.append(K)
    return key_stream

def rc4(text, key):
    """Chiffrement/Déchiffrement RC4 (même fonction pour les deux)"""
    key = [ord(c) for c in key]  # Convertir la clé en valeurs ASCII
    S = ksa(key)  # Initialisation de la S-Box
    #print(S)
    key_stream = prga(S, len(text))  # Génération du flot de clés
    result = [t ^ k for t, k in zip(text, key_stream)]  # XOR entre le texte et le flot de clés
    return bytes(result)

# Exemple d'utilisation
key = "secretkey"
message = "Hello, Milene!".encode()  # Conversion en bytes

# Chiffrement
ciphertext = rc4(message, key)
print("Texte chiffré (hex) :", ciphertext.hex())

# Déchiffrement (même fonction)
decrypted_text = rc4(ciphertext, key)
print("Texte déchiffré :", decrypted_text.decode())
