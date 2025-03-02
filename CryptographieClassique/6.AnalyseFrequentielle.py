from collections import Counter

def analyse_frequentielle(texte):
    """Analyse la fréquence des lettres dans un texte chiffré"""
    texte = texte.lower()  # Normalisation en minuscules
    lettres = [c for c in texte if c.isalpha()]  # Ne garder que les lettres
    total_lettres = len(lettres)

    # Comptage des fréquences
    compte = Counter(lettres)
    frequences = {lettre: (compte[lettre] / total_lettres) * 100 for lettre in compte}

    # Tri des lettres par fréquence décroissante
    frequences_triees = sorted(frequences.items(), key=lambda x: x[1], reverse=True)

    print("📊 Fréquence des lettres dans le texte chiffré :")
    for lettre, freq in frequences_triees:
        print(f"{lettre}: {freq:.2f}%")

    return frequences_triees

# Exemple de texte chiffré (monoalphabétique)
texte_chiffre = "LA PLUS BELLE PERSONNE AU MONDE C'EST TOI"  # Ex. avec substitution simple

# Exécution de l'analyse fréquentielle
analyse_frequentielle(texte_chiffre)
