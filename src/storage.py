"""Storage management."""
import json
from pathlib import Path

STORAGE_FILE = Path("data/passwords.json")

def load_passwords():
    """Load passwords from storage."""
    if not STORAGE_FILE.exists():
        return {}

    with open(STORAGE_FILE) as f:
        return json.load(f)
    
def save_passwords(passwords):
    """Save passwords to storage."""
    STORAGE_FILE.parent.mkdir(exist_ok=True)
    with open(STORAGE_FILE, 'w') as f:
        json.dump(passwords, f, indent=2)