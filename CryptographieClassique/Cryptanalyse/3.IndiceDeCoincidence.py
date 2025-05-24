import unicodedata
import string
from collections import Counter

def normalize_text(text):
    """
    Convertit le texte en minuscules et supprime les accents.
    """
    text = unicodedata.normalize('NFD', text)
    return ''.join(c for c in text if unicodedata.category(c) != 'Mn').lower()

def indice_coincidence(text):
    """
    Calcule l'indice de coïncidence (IC) d'un texte.
    La formule utilisée est : IC = sum(n_i*(n_i-1)) / (N*(N-1))
    où n_i est le nombre d'occurrences de chaque lettre et N le nombre total de lettres.
    """
    text = normalize_text(text)
    # Conserver uniquement les lettres a-z
    letters = [c for c in text if c in string.ascii_lowercase]
    N = len(letters)
    if N <= 1:
        return 0
    counts = Counter(letters)
    somme = sum(n * (n - 1) for n in counts.values())
    return somme / (N * (N - 1))

# Exemple d'utilisation
if __name__ == '__main__':
    texte_exemple = "La Cryptographie est l'art de coder et décoder des messages. C'est une discipline fascinante qui remonte à l'Antiquité."
    ic = indice_coincidence(texte_exemple)
    print(f"Indice de coïncidence : {ic:.4f}")
