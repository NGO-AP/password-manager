"""Tests voor de encryptie module in src/crypto.py."""
import sys
import os
import pytest

# Zorg dat Python de 'src' map kan vinden voor de import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from crypto import generate_key, encrypt, decrypt

def test_encryption_cycle():
    """Test of data hetzelfde blijft na encryptie en decryptie."""
    password = "MasterPassword123"
    message = "Dit is geheime informatie."
    
    # 1. Genereer key
    key = generate_key(password)
    
    # 2. Encrypt
    encrypted = encrypt(message, key)
    assert encrypted != message, "De versleutelde tekst mag niet gelijk zijn aan de leesbare tekst"
    
    # 3. Decrypt
    decrypted = decrypt(encrypted, key)
    assert decrypted == message, "De ontsleutelde tekst moet gelijk zijn aan het origineel"

def test_deterministic_key():
    """Test of hetzelfde wachtwoord altijd dezelfde key genereert."""
    password = "hetzelfde_wachtwoord"
    key1 = generate_key(password)
    key2 = generate_key(password)
    
    assert key1 == key2, "Hetzelfde wachtwoord moet altijd dezelfde key opleveren"

def test_invalid_token_with_wrong_key():
    """Test of decryptie faalt met een foutieve sleutel."""
    from cryptography.fernet import InvalidToken
    
    msg = "Top Secret"
    key_correct = generate_key("wachtwoord1")
    key_wrong = generate_key("wachtwoord2")
    
    encrypted = encrypt(msg, key_correct)
    
    with pytest.raises(InvalidToken):
        decrypt(encrypted, key_wrong)

if __name__ == "__main__":
    # Handmatig uitvoeren als script
    try:
        test_encryption_cycle()
        test_deterministic_key()
        print("✅ Alle basistests in tests/test_crypto.py zijn geslaagd!")
    except Exception as e:
        print(f"❌ Test gefaald: {e}")