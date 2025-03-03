from collections import Counter

def indice_de_coincidence(texte):
    texte = texte.upper()  # Convertir en majuscules pour uniformiser
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(texte)
    
    # Compter la fréquence de chaque lettre
    freq = Counter(lettre for lettre in texte if lettre in alphabet)
    
    # Calculer l'indice de coïncidence
    ic = sum(f * (f - 1) for f in freq.values()) / (n * (n - 1)) if n > 1 else 0
    
    return ic

# Exemple d'utilisation
texte_chiffre = "WXYZZWXYZZWXYZZWXYZ"  # Exemple de texte chiffré
ic = indice_de_coincidence(texte_chiffre)
print(f"Indice de coïncidence: {ic:.5f}")
