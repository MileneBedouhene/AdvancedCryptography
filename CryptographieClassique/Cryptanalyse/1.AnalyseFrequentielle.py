import unicodedata
import string
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def normalize_text(text):
    """
    Normalise le texte en supprimant les accents (ex: 'é' devient 'e').
    """
    text = unicodedata.normalize('NFD', text)
    return ''.join(c for c in text if unicodedata.category(c) != 'Mn')

def analyse_frequentielle(texte):
    """Analyse la fréquence des lettres dans un texte et retourne un dictionnaire.
       Les clés sont des lettres en minuscule et les valeurs leur pourcentage."""
    # Normalisation : conversion en minuscules et suppression des accents
    texte = normalize_text(texte.lower())
    # Ne conserver que les lettres de a à z
    lettres = [c for c in texte if c in string.ascii_lowercase]
    total_lettres = len(lettres)
    
    if total_lettres == 0:
        print("Aucune lettre trouvée dans le texte.")
        return {}
    
    # Comptage des lettres
    compte = Counter(lettres)
    frequences = {lettre: (compte[lettre] / total_lettres) * 100 for lettre in compte}
    
    # Affichage en console
    print("📊 Fréquence des lettres dans le texte :")
    for lettre, freq in sorted(frequences.items(), key=lambda x: x[1], reverse=True):
        print(f"{lettre}: {freq:.2f}%")
        
    return frequences

def plot_histogramme_with_expected(freq_obs, french_freq):
    """
    Affiche un histogramme comparant la fréquence observée dans le texte
    et la fréquence théorique en français pour chaque lettre.
    
    freq_obs : dictionnaire observé (lettres en minuscule -> pourcentage)
    french_freq : dictionnaire théorique (lettres en majuscule -> pourcentage)
    """
    lettres = list(string.ascii_uppercase)
    # Pour chaque lettre, récupérer la fréquence observée (0 si absente)
    obs = [freq_obs.get(letter.lower(), 0) for letter in lettres]
    exp = [french_freq.get(letter, 0) for letter in lettres]

    x = np.arange(len(lettres))  # positions des barres
    width = 0.35  # largeur des barres

    fig, ax = plt.subplots(figsize=(12, 6))
    rects1 = ax.bar(x - width/2, obs, width, label='Observé', color='skyblue')
    rects2 = ax.bar(x + width/2, exp, width, label='Théorique', color='lightgreen')

    ax.set_ylabel('Fréquence (%)')
    ax.set_title("Comparaison des fréquences des lettres : Observé vs. Théorique")
    ax.set_xticks(x)
    ax.set_xticklabels(lettres)
    ax.legend()

    # Annotation des barres
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.2f}%',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # Décalage vertical
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)

    plt.show()

# Distribution théorique des fréquences pour le français (en %)
FRENCH_FREQ = {
    'A': 7.636, 'B': 0.901, 'C': 3.260, 'D': 3.669, 'E': 14.715, 'F': 1.066,
    'G': 0.866, 'H': 0.737, 'I': 7.529, 'J': 0.613, 'K': 0.049, 'L': 5.456,
    'M': 2.968, 'N': 7.095, 'O': 5.796, 'P': 2.521, 'Q': 1.362, 'R': 6.693,
    'S': 7.948, 'T': 7.244, 'U': 6.311, 'V': 1.838, 'W': 0.049, 'X': 0.427,
    'Y': 0.128, 'Z': 0.326
}

# Exemple d'utilisation
if __name__ == '__main__':
    # Exemple de texte avec des accents et des majuscules/minuscules
    texte_chiffre = "Là plùs béllè pérsònné âù mónde, ç'est tɔî."
    
    # Analyse fréquentielle du texte
    freq_obs = analyse_frequentielle(texte_chiffre)
    
    # Affichage de l'histogramme comparatif
    plot_histogramme_with_expected(freq_obs, FRENCH_FREQ)
