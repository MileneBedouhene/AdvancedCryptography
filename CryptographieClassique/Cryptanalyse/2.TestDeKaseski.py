from collections import Counter
from math import gcd
from functools import reduce

# 1️⃣ Trouver les séquences répétées et calculer les écarts entre leurs apparitions
def find_repeated_sequences(ciphertext, min_length=3):
    sequences = {}
    for i in range(len(ciphertext) - min_length + 1):
        seq = ciphertext[i:i + min_length]
        if seq in sequences:
            sequences[seq].append(i)
        else:
            sequences[seq] = [i]

    gaps = []
    for seq, positions in sequences.items():
        if len(positions) > 1:
            for j in range(1, len(positions)):
                gaps.append(positions[j] - positions[j - 1])
    return gaps

# 2️⃣ Trouver la longueur probable de la clé
def find_key_length(ciphertext):
    gaps = find_repeated_sequences(ciphertext)
    if not gaps:
        return None
    return reduce(gcd, gaps)

# 3️⃣ Vérification des valeurs possibles du PGCD pour trouver la bonne longueur de clé
def test_multiple_key_lengths(ciphertext):
    gaps = find_repeated_sequences(ciphertext)
    if gaps:
        gcd_values = sorted(set(reduce(gcd, gaps[i:]) for i in range(len(gaps))), reverse=True)[:5]
        print(f"Valeurs possibles pour la longueur de la clé : {gcd_values}")
        return gcd_values
    return []

# 4️⃣ Diviser le texte en groupes selon la longueur de la clé
def split_text_by_key_length(text, key_length):
    groups = ['' for _ in range(key_length)]
    for i, char in enumerate(text):
        groups[i % key_length] += char
    return groups

# 5️⃣ Trouver le décalage de chaque groupe en supposant que 'E' est la lettre la plus fréquente
def find_caesar_shift(text_group):
    letter_counts = Counter(text_group)
    most_common_letter = letter_counts.most_common(1)[0][0]  # Lettre la plus fréquente
    shift = (ord(most_common_letter) - ord('E')) % 26  # Décalage vers 'E'
    return shift

# 6️⃣ Déduire la clé de Vigenère
def find_vigenere_key(ciphertext, key_length):
    text_groups = split_text_by_key_length(ciphertext, key_length)
    shifts = [find_caesar_shift(group) for group in text_groups]
    key = ''.join(chr(ord('A') + shift) for shift in shifts)
    print(f"Décalages trouvés : {shifts}")
    return key

# 7️⃣ Déchiffrement avec la clé trouvée
def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        shift = ord(key[i % key_length]) - ord('A')
        decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)

# 🚀 Exécution du script
if __name__ == "__main__":
    ciphertext = "XINVLTFWRVNTTQPIKIDKPYAVATPIFWQVEMRPPIYWYEBZZXRGFQZRQIELZRAIQAOEAWZWEVRIDMYYZIDQBYRIZAPGHVUALRGPQAPGUEZOPWQMZNZVZEFQZRFIXTPTRVYMEHRKMZLRGMDTLGBRRQOIAXUIWMGIPMDHBRZMPWFIZATFYIEOCEPIMLPWNPSWCMGLYMDHRGTQQJEIYMYXNZMVNIFPQAOSARQMDWBRFBCEAWRWCQRIEMYJBVYIEWVPXQDMOPQACIAHMVEMZTAADMOPQTPYEEOKPWCEDLPWCIDAZRAIEVZRNYFWCMFIQANIYEQAETNVFQNYYMQZPQRRFKCYPMMTOEAWPMDHBQMQYIFXQTDUHIXMDXEEZALGGMAVDJVRMVNMRVQAWIFGAUXYAMOIEMBREUPHVGMTPWRXXMDIPLMVRIFHUVQSEQMBTSAWBMCWBRZMWPRW"

    # Étape 1 : Détecter la longueur de la clé
    key_length = find_key_length(ciphertext)
    print(f"Longueur probable de la clé : {key_length}")

    # Étape 2 : Vérifier d'autres longueurs possibles si la clé semble fausse
    possible_lengths = test_multiple_key_lengths(ciphertext)

    # Essayer avec la meilleure longueur détectée
    if key_length and key_length in possible_lengths:
        key = find_vigenere_key(ciphertext, 6)
        print(f"Clé trouvée : {key}")

        decrypted_text = vigenere_decrypt(ciphertext, key)
        print(f"\nTexte déchiffré :\n{decrypted_text}")
    else:
        print("Impossible de déterminer la bonne longueur de clé. Vérifiez les valeurs détectées.")

