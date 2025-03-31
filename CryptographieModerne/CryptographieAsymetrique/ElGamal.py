import random
from sympy import isprime

def generate_large_prime():
    """ Génère un grand nombre premier """
    while True:
        prime = random.randint(100, 500)
        if isprime(prime):
            return prime

def mod_exp(base, exp, mod):
    """ Exponentiation modulaire """
    return pow(base, exp, mod)

# Génération des clés
p = generate_large_prime()  # Nombre premier
g = random.randint(2, p - 1)  # Générateur
x = random.randint(2, p - 2)  # Clé privée
h = mod_exp(g, x, p)  # Clé publique

def encrypt(message, p, g, h):
    y = random.randint(2, p - 2)
    c1 = mod_exp(g, y, p)
    c2 = (message * mod_exp(h, y, p)) % p
    return c1, c2

def decrypt(c1, c2, x, p):
    s = mod_exp(c1, x, p)  # Calcul du secret
    s_inv = pow(s, -1, p)  # Inverse modulaire
    message = (c2 * s_inv) % p
    return message

# Simulation du chiffrement-déchiffrement
message = 42  # Un message à chiffrer (doit être < p)
c1, c2 = encrypt(message, p, g, h)
decrypted_message = decrypt(c1, c2, x, p)

# Affichage des résultats
print(f"Nombre premier (p): {p}")
print(f"Générateur (g): {g}")
print(f"Clé privée (x): {x}")
print(f"Clé publique (h): {h}")
print(f"Message chiffré: (c1={c1}, c2={c2})")
print(f"Message déchiffré: {decrypted_message}")
