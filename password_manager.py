from storage import init_vault, load_vault, save_vault
import secrets, string

def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def main():
    master = input("Enter master password: ")
    key = init_vault(master)
    vault = load_vault(key)

    while True:
        print("\nOptions: [1] Add [2] Get [3] Delete [4] Generate [5] Exit")
        choice = input("Choose: ")
        if choice == "1":
            site = input("Site: ")
            user = input("Username: ")
            pw = input("Password (leave blank to generate): ")
            if not pw:
                pw = generate_password()
                print(f"Generated password: {pw}")
            vault[site] = {"username": user, "password": pw}
            save_vault(vault, key)
            print("Saved.")
        elif choice == "2":
            site = input("Site to retrieve: ")
            entry = vault.get(site)
            print(entry if entry else "Not found.")
        elif choice == "3":
            site = input("Site to delete: ")
            vault.pop(site, None)
            save_vault(vault, key)
            print("Deleted (if existed).")
        elif choice == "4":
            print("Generated password:", generate_password())
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
