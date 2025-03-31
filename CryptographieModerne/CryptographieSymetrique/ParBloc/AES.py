from Crypto.Cipher import AES
from Crypto import Random

def pad(msg):
    """Ajoute un padding PKCS#7 pour atteindre un multiple de 16 octets (AES)"""
    padding_len = 16 - (len(msg) % 16)
    return msg + chr(padding_len) * padding_len

def unpad(msg):
    """Supprime le padding PKCS#7 après déchiffrement"""
    return msg[:-ord(msg[-1])]

def Aes_Encrypt(msg, mode):
    """Chiffrement AES avec mode ECB ou CBC (Sortie en hexadécimal)"""
    block_size = AES.block_size  # 16 octets pour AES
    key = Random.get_random_bytes(16)  # Clé AES-128 (16 octets)
    iv = Random.get_random_bytes(16) if mode == 'CBC' else None  # IV pour CBC

    cipher = AES.new(key, AES.MODE_ECB) if mode == 'ECB' else AES.new(key, AES.MODE_CBC, iv)
    padded_msg = pad(msg)
    encrypted_message = cipher.encrypt(padded_msg.encode('utf-8'))

    # Affichage des résultats
    print("\n🔐 Chiffrement AES réussi :")
    print("Clé (hex) :", key.hex())
    if iv:
        print("IV (hex) :", iv.hex())
    print("Message chiffré (hex) :", encrypted_message.hex())
    
    return key, iv, encrypted_message.hex()

def Aes_Decrypt():
    """Déchiffrement AES avec mode ECB ou CBC (Entrée en hexadécimal)"""
    key_hex = input("\nEntrez la clé AES (16 octets en hex) : ")
    key = bytes.fromhex(key_hex)
    mode = input("Mode (ECB / CBC) : ").strip().upper()

    if mode not in ['ECB', 'CBC']:
        print("❌ Mode invalide !")
        return
    
    iv = None
    if mode == 'CBC':
        iv_hex = input("Entrez l'IV (16 octets en hex) : ")
        iv = bytes.fromhex(iv_hex)

    msg_encrypted_hex = input("Message chiffré (en hex) : ")
    encrypted_message = bytes.fromhex(msg_encrypted_hex)

    cipher = AES.new(key, AES.MODE_ECB) if mode == 'ECB' else AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = cipher.decrypt(encrypted_message)

    print("\n🔓 Message déchiffré :", unpad(decrypted_message.decode('utf-8')))

# Exemple d'utilisation
if __name__ == "__main__":
    message = input("Message à chiffrer : ")
    mode = input("Mode (ECB / CBC) : ").strip().upper()

    if mode not in ['ECB', 'CBC']:
        print("❌ Mode invalide !")
    else:
        key, iv, encrypted_message = Aes_Encrypt(message, mode)
        Aes_Decrypt()  # Déchiffrement interactif