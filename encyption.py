from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def initialize_cipher(key):
    return Fernet(key)

def encrypt(cipher, password):
    return cipher.encrypt(password.encode()).decode()

def decrypt(cipher, encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()