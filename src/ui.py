"""User interface."""

def show_menu():
    """Display main menu."""
    print("\n" + "="*40)
    print("PASSWORD MANAGER")
    print("="*40)
    print("1. Add password")
    print("2. Get password")
    print("3. List accounts")
    print("4. Generate password")
    print("5. Exit")
    print("="*40)

def get_choice():
    """Get user menu choice."""
    return input("\nChoice: ").strip()