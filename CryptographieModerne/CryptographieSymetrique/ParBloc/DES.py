from Crypto.Cipher import DES
from Crypto import Random

def pad(msg):
    """Ajoute un padding pour atteindre un multiple de 8 octets"""
    padding_len = 8 - (len(msg) % 8)
    return msg + chr(padding_len) * padding_len

def unpad(msg):
    """Supprime le padding ajouté après déchiffrement"""
    return msg[:-ord(msg[-1])]

def Des_Encrypt(msg, mode):
    """Chiffrement DES avec mode ECB ou CBC (Sortie en hexadécimal)"""
    block_size = DES.block_size  # 8 octets
    key = Random.get_random_bytes(8)  # Génère une clé de 8 octets
    iv = Random.get_random_bytes(8) if mode == 'CBC' else None  # Génère un IV pour CBC

    cipher = DES.new(key, DES.MODE_ECB) if mode == 'ECB' else DES.new(key, DES.MODE_CBC, iv)
    padded_msg = pad(msg)
    encrypted_message = cipher.encrypt(padded_msg.encode('utf-8'))

    # Affichage des résultats
    print("\n🔐 Chiffrement réussi :")
    print("Clé (en hexadécimal) :", key.hex())
    if iv:
        print("IV (en hexadécimal) :", iv.hex())
    print("Message chiffré (en hexadécimal) :", encrypted_message.hex())
    
    return key, iv, encrypted_message.hex()

def Des_Decrypt():
    """Déchiffrement DES avec mode ECB ou CBC (Entrée en hexadécimal)"""
    key_hex = input("\nEntrez la clé en hexadécimal : ")
    key = bytes.fromhex(key_hex)
    mode = input("Choisissez le mode (ECB / CBC) : ").strip().upper()

    if mode not in ['ECB', 'CBC']:
        print("❌ Mode invalide !")
        return
    
    iv = None
    if mode == 'CBC':
        iv_hex = input("Entrez l'IV en hexadécimal : ")
        iv = bytes.fromhex(iv_hex)

    msg_encrypted_hex = input("Entrez le message chiffré (en hexadécimal) : ")
    encrypted_message = bytes.fromhex(msg_encrypted_hex)

    cipher = DES.new(key, DES.MODE_ECB) if mode == 'ECB' else DES.new(key, DES.MODE_CBC, iv)
    decrypted_message = cipher.decrypt(encrypted_message)

    print("\n🔓 Message déchiffré :", unpad(decrypted_message.decode('utf-8')))

# Exemple de chiffrement
message = input("Entrez le message à chiffrer : ")
mode = input("Choisissez le mode (ECB / CBC) : ").strip().upper()

if mode not in ['ECB', 'CBC']:
    print("❌ Mode invalide !")
else:
    key, iv, encrypted_message = Des_Encrypt(message, mode)

    # Déchiffrement
    Des_Decrypt()
