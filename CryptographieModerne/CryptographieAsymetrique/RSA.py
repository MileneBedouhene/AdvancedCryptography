from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def generate_rsa_keys():
    """Génère une paire de clés RSA (2048 bits)"""
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def Rsa_Encrypt(msg, public_key):
    """Chiffre un message avec RSA (sortie en hexadécimal)"""
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted = cipher.encrypt(msg.encode())
    return binascii.hexlify(encrypted).decode()

def Rsa_Decrypt(encrypted_hex, private_key):
    """Déchiffre un message RSA (entrée en hexadécimal)"""
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted = cipher.decrypt(binascii.unhexlify(encrypted_hex))
    return decrypted.decode()

def main():
    print("\n🔑 Génération des clés RSA (2048 bits)...")
    private_key, public_key = generate_rsa_keys()
    
    print("\nClé privée (PEM) :\n", private_key.decode())
    print("\nClé publique (PEM) :\n", public_key.decode())

    # Chiffrement
    message = input("\nEntrez le message à chiffrer : ")
    encrypted_msg = Rsa_Encrypt(message, public_key)
    print("\n🔐 Message chiffré (hex) :", encrypted_msg)

    # Déchiffrement
    input("\nAppuyez sur Entrée pour déchiffrer...")
    decrypted_msg = Rsa_Decrypt(encrypted_msg, private_key)
    print("\n🔓 Message déchiffré :", decrypted_msg)

if __name__ == "__main__":
    main()