import random

def generate_private_key(prime):
    """ Génère une clé privée aléatoire """
    return random.randint(2, prime - 2)

def compute_public_key(base, private_key, prime):
    """ Calcule la clé publique """
    return pow(base, private_key, prime)

def compute_shared_secret(public_key, private_key, prime):
    """ Calcule le secret partagé """
    return pow(public_key, private_key, prime)

# Paramètres publics (doivent être connus par Alice et Bob)
prime = 23  # Nombre premier (P)
base = 5    # Base génératrice (G)

# Clé privée d'Alice
alice_private = generate_private_key(prime)
alice_public = compute_public_key(base, alice_private, prime)

# Clé privée de Bob
bob_private = generate_private_key(prime)
bob_public = compute_public_key(base, bob_private, prime)

# Échange de clés et calcul du secret partagé
alice_shared_secret = compute_shared_secret(bob_public, alice_private, prime)
bob_shared_secret = compute_shared_secret(alice_public, bob_private, prime)

# Affichage des résultats
print(f"Clé privée d'Alice: {alice_private}")
print(f"Clé publique d'Alice: {alice_public}")
print(f"Clé privée de Bob: {bob_private}")
print(f"Clé publique de Bob: {bob_public}")
print(f"Secret partagé d'Alice: {alice_shared_secret}")
print(f"Secret partagé de Bob: {bob_shared_secret}")

# Vérification que le secret partagé est identique
print(f"Les secrets sont égaux ?", alice_shared_secret == bob_shared_secret)
