from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Génération des clés
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Chiffrement avec la clé publique
def rsa_encrypt(message, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted = cipher.encrypt(message.encode())
    return binascii.hexlify(encrypted).decode()

# Déchiffrement avec la clé privée
def rsa_decrypt(encrypted_message, private_key):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted = cipher.decrypt(binascii.unhexlify(encrypted_message))
    return decrypted.decode()

# Exemple
message = "Hello RSA!"
encrypted = rsa_encrypt(message, public_key)
decrypted = rsa_decrypt(encrypted, private_key)

print(f"Message original: {message}")
print(f"Chiffré: {encrypted}")
print(f"Déchiffré: {decrypted}")