"""Encryption and decryption using Fernet."""
from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(master_password):
    """Generate encryption key from master password."""
    # Hash password to get 32 bytes key
    key = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt(data, key):
    """Encrypt data with key."""
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def decrypt(encrypted_data, key):
    """Decrypt data with key."""
    f = Fernet(key)
    return f.decrypt(encrypted_data.encode()).decode()