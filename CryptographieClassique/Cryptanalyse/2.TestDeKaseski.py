from collections import defaultdict
import math

def find_repeated_sequences(texte, longueur_min=3):
    """ Trouve les séquences répétées dans le texte chiffré et leurs positions """
    sequences = defaultdict(list)
    for i in range(len(texte) - longueur_min + 1):
        sequence = texte[i:i+longueur_min]
        sequences[sequence].append(i)
    
    # Ne garder que les séquences qui apparaissent plusieurs fois
    return {seq: pos for seq, pos in sequences.items() if len(pos) > 1}

def compute_distances(repeated_sequences):
    """ Calcule les distances entre les occurrences des séquences répétées """
    distances = []
    for positions in repeated_sequences.values():
        for i in range(len(positions) - 1):
            distances.append(positions[i+1] - positions[i])
    return distances

def gcd_of_list(numbers):
    """ Calcule le PGCD (Plus Grand Commun Diviseur) des distances """
    return math.gcd(*numbers) if numbers else None

def kasiski_examination(texte, longueur_min=3):
    """ Applique le test de Kasiski pour estimer la longueur de la clé """
    texte = texte.replace(" ", "").upper()  # Supprimer les espaces et mettre en majuscules
    
    # Étape 1 : Trouver les séquences répétées
    repeated_sequences = find_repeated_sequences(texte, longueur_min)
    print("🔍 Séquences répétées trouvées :", repeated_sequences)

    # Étape 2 : Calculer les distances entre les occurrences
    distances = compute_distances(repeated_sequences)
    print("📏 Distances entre occurrences :", distances)

    # Étape 3 : Trouver le PGCD des distances
    key_length = gcd_of_list(distances)
    print("🔑 Longueur estimée de la clé :", key_length)
    
    return key_length

# Exemple de texte chiffré (Vigenère)
texte_chiffre = "LXFOPVEFRNHRLXFOPVEFRNHR"

# Exécution du test de Kasiski
kasiski_examination(texte_chiffre)
