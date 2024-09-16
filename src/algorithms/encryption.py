# encryption.py

def encrypt(message, key):
    # Simple XOR encryption for demonstration purposes
    return ''.join(str(int(m) ^ int(k)) for m, k in zip(message, key))

def decrypt(encrypted_message, key):
    # Simple XOR decryption (same as encryption for XOR)
    return ''.join(str(int(e) ^ int(k)) for e, k in zip(encrypted_message, key))