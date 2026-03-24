"""Password Manager - Main entry point."""
import sys
from getpass import getpass

from src.authenticator import setup_master_password, verify_master_password
from src.storage import load_passwords, save_passwords
from src.crypto import generate_key, encrypt, decrypt
from src.generator import generate_password
from src.ui import show_menu, get_choice

def main():
    """Main application loop."""
    # Check if first run
    from pathlib import Path
    if not Path("data/master.hash").exists():
        print("First time setup")
        master = getpass("Create master password: ")
        confirm = getpass("Confirm master password: ")

        if master != confirm:
            print("Passwords don't match!")
            sys.exit(1)

        setup_master_password(master)
        print("Master password created!\n")

    # Authenticate
    master = getpass("Enter master password: ")
    if not verify_master_password(master):
        print("Invalid password!")
        sys.exit(1)

    # Generate encryption key
    key = generate_key(master)

    # Load passwords
    passwords = load_passwords()

    # Main loop
    while True:
        show_menu()
        choice = get_choice()

        if choice == "1":
            # Add password
            account = input("Account name: ")
            password = getpass("Password (leave empty to generate): ")

            if not password:
                password = generate_password()
                print(f"Generated: {password}")

            encrypted = encrypt(password, key)
            passwords[account] = encrypted
            save_passwords(passwords)
            print(f"Saved password for {account}")

        elif choice == "2":
            # Get password
            account = input("Account name: ")
            if account in passwords:
                decrypted = decrypt(passwords[account], key)
                print(f"Password: {decrypted}")
            else:
                print("Account not found")

        elif choice == "3":
            # List accounts
            if passwords:
                print("\nStored accounts:")
                for account in passwords:
                    print(f" - {account}")
            else:
                print("No passwords stored")

        elif choice == "4":
            # Generate password
            length = int(input("Length (default 16): ") or 16)
            password = generate_password(length)
            print(f"Generated: {password}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
 main()
