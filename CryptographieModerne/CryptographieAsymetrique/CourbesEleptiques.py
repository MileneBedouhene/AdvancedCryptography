from tinyec import registry
import secrets

def generate_keypair(curve):
    """ Génère une paire de clés (privée et publique) """
    private_key = secrets.randbelow(curve.field.n)
    public_key = private_key * curve.g
    return private_key, public_key

def compute_shared_secret(private_key, public_key):
    """ Calcule le secret partagé """
    shared_secret = private_key * public_key
    return shared_secret

# Choix d'une courbe elliptique
curve = registry.get_curve("secp192r1")

# Génération des clés pour Alice et Bob
alice_private, alice_public = generate_keypair(curve)
bob_private, bob_public = generate_keypair(curve)

# Calcul des secrets partagés
alice_shared = compute_shared_secret(alice_private, bob_public)
bob_shared = compute_shared_secret(bob_private, alice_public)

# Affichage des résultats
print(f"Clé privée d'Alice: {alice_private}")
print(f"Clé publique d'Alice: ({alice_public.x}, {alice_public.y})")
print(f"Clé privée de Bob: {bob_private}")
print(f"Clé publique de Bob: ({bob_public.x}, {bob_public.y})")
print(f"Secret partagé d'Alice: ({alice_shared.x}, {alice_shared.y})")
print(f"Secret partagé de Bob: ({bob_shared.x}, {bob_shared.y})")
print(f"Les secrets sont identiques ? {alice_shared == bob_shared}")
