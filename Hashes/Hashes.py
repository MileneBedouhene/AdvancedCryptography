import hashlib

def generate_hashes(message):
    # Création d'un dictionnaire pour stocker les résultats
    hashes = {}
    
    # Hash MD5
    hashes['MD5'] = hashlib.md5(message.encode()).hexdigest()
    
    # Hash SHA-1
    hashes['SHA-1'] = hashlib.sha1(message.encode()).hexdigest()
    
    # Hash SHA-224
    hashes['SHA-224'] = hashlib.sha224(message.encode()).hexdigest()
    
    # Hash SHA-256
    hashes['SHA-256'] = hashlib.sha256(message.encode()).hexdigest()
    
    # Hash SHA-384
    hashes['SHA-384'] = hashlib.sha384(message.encode()).hexdigest()
    
    # Hash SHA-512
    hashes['SHA-512'] = hashlib.sha512(message.encode()).hexdigest()
    
    # Ajouter d'autres algorithmes si nécessaire, par exemple :
    # hashes['SHA-3-256'] = hashlib.sha3_256(message.encode()).hexdigest()
    # hashes['SHA-3-512'] = hashlib.sha3_512(message.encode()).hexdigest()
    
    return hashes

# Exemple d'utilisation
message = input("Entrez le message à hasher: ")
hashes = generate_hashes(message)

print("\nHashes générés:")
for algo, hash_value in hashes.items():
    print(f"{algo}: {hash_value}")
