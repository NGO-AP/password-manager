"""Password generation."""
import random
import string

def generate_password(length=16, use_special=True):
    """Generate random secure password."""
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password
