import socket
import struct
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes

# Connect to server
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(60)  # 60-second timeout
    server_ip = "192.168.153.137"  
    client.connect((server_ip, 9999))
    print(f"Connected to server at {server_ip}:9999")
except Exception as e:
    print(f"Error connecting to server: {e}")
    exit(1)

# Receive public key from server
try:
    public_key = client.recv(4096)
    if not public_key:
        raise ValueError("No public key received")
    key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(key)
    print("Received public key from server")
except Exception as e:
    print(f"Error receiving public key: {e}")
    client.close()
    exit(1)

# Generate and encrypt AES key
try:
    aes_key = get_random_bytes(16)
    encrypted_key = cipher_rsa.encrypt(aes_key)
    client.send(encrypted_key)
    print("Sent encrypted AES key")
except Exception as e:
    print(f"Error generating/sending AES key: {e}")
    client.close()
    exit(1)

# Live communication loop
try:
    while True:
        # Send message
        message = input("Client (type 'quit' to exit): ").encode()
        cipher_aes = AES.new(aes_key, AES.MODE_EAX)
        nonce = cipher_aes.nonce
        ciphertext, tag = cipher_aes.encrypt_and_digest(message)
        msg_data = nonce + ciphertext + tag
        client.send(struct.pack('!I', len(msg_data)) + msg_data)
        print("Sent encrypted message")
        if message.decode().lower() == "quit":
            print("Client sent quit command")
            break

        # Receive response
        length_data = client.recv(4)
        if not length_data:
            print("Server disconnected")
            break
        msg_length = struct.unpack('!I', length_data)[0]
        data = client.recv(msg_length)
        if len(data) != msg_length:
            print(f"Error: Expected {msg_length} bytes, got {len(data)}")
            continue

        nonce = data[:16]
        ciphertext = data[16:-16]
        tag = data[-16:]
        try:
            cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
            decrypted_response = cipher_aes.decrypt_and_verify(ciphertext, tag)
            response = decrypted_response.decode()
            print(f"Received response: {response}")
            if response.lower() == "quit":
                print("Server sent quit command")
                break
        except ValueError as e:
            print(f"Decryption error: {e}")
            continue

except Exception as e:
    print(f"Error in communication loop: {e}")
finally:
    client.close()
    print("Client closed")