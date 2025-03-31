from Crypto.Cipher import Blowfish
from Crypto import Random
import base64

# Fonction de padding (PKCS7)
def pad(s):
    padding_len = Blowfish.block_size - (len(s) % Blowfish.block_size)
    return s + bytes([padding_len] * padding_len)

def unpad(s):
    return s[:-s[-1]]

# Chiffrement en mode CBC
def BlowEncrypt_CBC(msg, key):
    iv = Random.new().read(Blowfish.block_size)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    encrypted_message = iv + cipher.encrypt(pad(msg.encode('utf-8')))
    return base64.b64encode(encrypted_message).decode('utf-8')

# Déchiffrement en mode CBC
def BlowDecrypt_CBC(key, encrypted_message):
    encrypted_message = base64.b64decode(encrypted_message)
    iv = encrypted_message[:Blowfish.block_size]
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(encrypted_message[Blowfish.block_size:]))
    return decrypted_message.decode('utf-8')

# Chiffrement en mode ECB (pas de IV ici)
def BlowEncrypt_ECB(msg, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    encrypted_message = cipher.encrypt(pad(msg.encode('utf-8')))
    return base64.b64encode(encrypted_message).decode('utf-8')

# Déchiffrement en mode ECB
def BlowDecrypt_ECB(key, encrypted_message):
    encrypted_message = base64.b64decode(encrypted_message)
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted_message = unpad(cipher.decrypt(encrypted_message))
    return decrypted_message.decode('utf-8')

# Exemple d'utilisation
key = Random.new().read(16)  # La clé doit être de 16 octets
message = "Hello, Blowfish!"

# Test CBC
encrypted_CBC = BlowEncrypt_CBC(message, key)
decrypted_CBC = BlowDecrypt_CBC(key, encrypted_CBC)

print(f"Mode CBC - Message chiffré : {encrypted_CBC}")
print(f"Mode CBC - Message déchiffré : {decrypted_CBC}")

# Test ECB
encrypted_ECB = BlowEncrypt_ECB(message, key)
decrypted_ECB = BlowDecrypt_ECB(key, encrypted_ECB)

print(f"\nMode ECB - Message chiffré : {encrypted_ECB}")
print(f"Mode ECB - Message déchiffré : {decrypted_ECB}")
