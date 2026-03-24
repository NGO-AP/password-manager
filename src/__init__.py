"""Package initialisatie."""

print("Password manager package geladen")

import logging
logging.basicConfig(level=logging.INFO)

__version__ = "1.0.0"
__author__ = "Niels Gonnissen"

__all__ = [
    'generate_key', 'encrypt', 'decrypt',
    'generate_password', 'load_passwords', 'save_passwords',
    'hash_password', 'setup_master_password', 'verify_master_password', 'show_menu', 'get_choice'
]