import socket
import struct
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes

# Generate RSA key pair
try:
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    # Save private key (optional)
    with open("private.pem", "wb") as f:
        f.write(private_key)
except Exception as e:
    print(f"Error generating RSA keys: {e}")
    exit(1)

# Load private key
try:
    key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(key)
except Exception as e:
    print(f"Error loading private key: {e}")
    exit(1)

# Set up server socket
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 9999))
    server.listen(1)
    print("Server listening on port 9999...")
except Exception as e:
    print(f"Error setting up server socket: {e}")
    exit(1)

# Accept client connection
try:
    conn, addr = server.accept()
    print(f"Connected by {addr}")
except Exception as e:
    print(f"Error accepting connection: {e}")
    server.close()
    exit(1)

# Send public key to client
try:
    conn.send(public_key)
    print("Sent public key to client")
except Exception as e:
    print(f"Error sending public key: {e}")
    conn.close()
    server.close()
    exit(1)

# Receive and decrypt AES key
try:
    encrypted_aes_key = conn.recv(256)
    if len(encrypted_aes_key) != 256:
        raise ValueError(f"Expected 256 bytes for AES key, got {len(encrypted_aes_key)}")
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)
    print("Received and decrypted AES key")
except Exception as e:
    print(f"Error receiving/decrypting AES key: {e}")
    conn.close()
    server.close()
    exit(1)

# Live communication loop
try:
    conn.settimeout(60)  # 60-second timeout for receiving messages
    while True:
        # Receive message length
        length_data = conn.recv(4)
        if not length_data:
            print("Client disconnected")
            break
        msg_length = struct.unpack('!I', length_data)[0]

        # Receive nonce + ciphertext + tag
        data = conn.recv(msg_length)
        if len(data) != msg_length:
            print(f"Error: Expected {msg_length} bytes, got {len(data)}")
            continue

        nonce = data[:16]
        ciphertext = data[16:-16]
        tag = data[-16:]

        # Decrypt message
        try:
            cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
            decrypted_message = cipher_aes.decrypt_and_verify(ciphertext, tag)
            message = decrypted_message.decode()
            print(f"Received message: {message}")
            if message.lower() == "quit":
                print("Client sent quit command")
                break
        except ValueError as e:
            print(f"Decryption error: {e}")
            continue

        # Get response from user
        response = input("Server (type 'quit' to exit): ").encode()
        cipher_aes = AES.new(aes_key, AES.MODE_EAX)
        nonce = cipher_aes.nonce
        ciphertext, tag = cipher_aes.encrypt_and_digest(response)
        msg_data = nonce + ciphertext + tag
        conn.send(struct.pack('!I', len(msg_data)) + msg_data)
        print("Sent response to client")
        if response.decode().lower() == "quit":
            print("Server sent quit command")
            break

except Exception as e:
    print(f"Error in communication loop: {e}")
finally:
    conn.close()
    server.close()
    print("Server closed")