"""Master password authentication."""
import hashlib
from pathlib import Path

MASTER_FILE = Path("data/master.hash")

def hash_password(password):
    """Hash password for storage."""
    return hashlib.sha256(password.encode()).hexdigest()

def setup_master_password(password):
    """Setup initial master password."""
    MASTER_FILE.parent.mkdir(exist_ok=True)
    with open(MASTER_FILE, 'w') as f:
        f.write(hash_password(password))

def verify_master_password(password):
    """Verify master password."""
    if not MASTER_FILE.exists():
        return False

    with open(MASTER_FILE) as f:
        stored_hash = f.read().strip()

    return hash_password(password) == stored_hash