import re
from collections import defaultdict, Counter

# Fréquence des lettres en français
FRENCH_LETTER_FREQ = {
    'E': 14.7, 'A': 7.6, 'I': 7.5, 'S': 7.9, 'T': 7.2, 'N': 7.0,
    'R': 6.9, 'U': 6.3, 'L': 5.4, 'O': 5.1, 'D': 3.6, 'C': 3.3,
    'M': 2.9, 'P': 2.9, 'G': 1.2, 'B': 1.1, 'V': 1.1, 'H': 1.1,
    'F': 1.1, 'Q': 1.0, 'Y': 0.4, 'X': 0.4, 'J': 0.3, 'K': 0.1, 'W': 0.1, 'Z': 0.1
}

def find_repeated_sequences(ciphertext, seq_length=3):
    sequences = defaultdict(list)
    for i in range(len(ciphertext) - seq_length + 1):
        seq = ciphertext[i:i + seq_length]
        sequences[seq].append(i)
    return {seq: positions for seq, positions in sequences.items() if len(positions) > 1}

def find_distances(repeated_sequences):
    distances = []
    for positions in repeated_sequences.values():
        for i in range(1, len(positions)):
            distances.append(positions[i] - positions[i - 1])
    return distances

def find_common_factors(distances):
    factors = defaultdict(int)
    for distance in distances:
        for factor in range(2, distance + 1):
            if distance % factor == 0:
                factors[factor] += 1
    return sorted(factors.items(), key=lambda x: x[1], reverse=True)

def kasiski_test(ciphertext, seq_length=3):
    repeated_sequences = find_repeated_sequences(ciphertext, seq_length)
    distances = find_distances(repeated_sequences)
    if not distances:
        return "Aucune répétition trouvée."
    key_length_candidates = find_common_factors(distances)
    return key_length_candidates

def split_text_into_columns(ciphertext, key_length):
    columns = ['' for _ in range(key_length)]
    for i, char in enumerate(ciphertext):
        columns[i % key_length] += char
    return columns

def caesar_shift_analysis(column):
    letter_counts = Counter(column)
    most_common_letter, _ = letter_counts.most_common(1)[0]
    
    # Chercher le décalage par rapport à 'E' (lettre la plus fréquente en français)
    shift = (ord(most_common_letter) - ord('E')) % 26
    return chr(shift + ord('A'))  # Convertir en lettre majuscule

def determine_key(ciphertext, key_length):
    columns = split_text_into_columns(ciphertext, key_length)
    key = ''.join(caesar_shift_analysis(col) for col in columns)
    return key

# Test complet
ciphertext = "CLCJSGEEXJGGOETFEUUUPEIRMOOBTGGRCOAKTLCHRCODGGO" \
             "TDEFVCJJFHSEFFVKHEPFRGFSVRUGMAOFMGMEVURGTETBCJJF" \
             "HSEGEEFJFHFRGOTGTMCOIGSEUMEEIIHGRGEEXJGGOETFEZJGG" \
             "DOONERSEURUGMAVPTCMIVFDGTSATTGNEUEEEIIHGRGNEPUQ"

# 1. Test de Kasiski
key_length_candidates = kasiski_test(ciphertext)
print("Longueurs de clé possibles :", key_length_candidates)

# 2. Prendre la longueur la plus probable (ex: première du tableau)
if key_length_candidates:
    probable_key_length = key_length_candidates[0][0]
    print("Longueur probable de la clé :", probable_key_length)

    # 3. Déterminer la clé avec l'analyse fréquentielle
    key = determine_key(ciphertext, probable_key_length)
    print("Clé trouvée :", key)
