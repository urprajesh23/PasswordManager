import mysql.connector
from cryptography.fernet import Fernet
import os

# Generate and load encryption key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", 'rb') as key_file:
        key = key_file.read()
    return key

# Create the key if it doesn't exist
if not os.path.exists("key.key"):
    write_key()

key = load_key()
fer = Fernet(key)

# Connect to the SQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2006",
    database="PwdDB"
)

cursor = db.cursor()

def view_passwords():
    cursor.execute("SELECT platform, username, password FROM Passwords")
    results = cursor.fetchall()
    if results:
        for row in results:
            platform, username, encrypted_password = row
            decrypted_password = fer.decrypt(encrypted_password.encode()).decode()
            print("\nPlatform:", platform)
            print("Username:", username)
            print("Password:", decrypted_password)
    else:
        print("No stored passwords found.")

def add_password():
    platform = input("Enter the platform name: ")
    a_name = input("Enter the account name: ")
    a_pwd = input("Enter the account password: ")
    encrypted_pwd = fer.encrypt(a_pwd.encode()).decode()

    cursor.execute("INSERT INTO Passwords (platform, username, password) VALUES (%s, %s, %s)", 
                   (platform, a_name, encrypted_pwd))
    db.commit()
    print("Successfully added.")

def delete_password():
    platform_to_delete = input("Enter the platform name whose password you want to delete: ")
    cursor.execute("DELETE FROM Passwords WHERE platform = %s", (platform_to_delete,))
    db.commit()
    if cursor.rowcount > 0:
        print(f"Deleted password entry for platform: {platform_to_delete}")
    else:
        print(f"No password found for platform: {platform_to_delete}")

def update_password_or_username():
    platform_to_update = input("Enter the platform name whose password/username you want to update: ")
    
    # Check if the platform exists
    cursor.execute("SELECT platform FROM Passwords WHERE platform = %s", (platform_to_update,))
    if cursor.fetchone():
        print("\nWhat would you like to update?")
        print("1. Username")
        print("2. Password")
        update_choice = input("Enter '1' to update the username or '2' to update the password: ").strip()
        
        if update_choice == "2":
            new_password = input("Enter the new password: ")
            encrypted_pwd = fer.encrypt(new_password.encode()).decode()
            cursor.execute("UPDATE Passwords SET password = %s WHERE platform = %s", 
                           (encrypted_pwd, platform_to_update))
            db.commit()
            print(f"Password for {platform_to_update} updated successfully.")
            
        elif update_choice == "1":
            new_username = input("Enter the new username: ")
            cursor.execute("UPDATE Passwords SET username = %s WHERE platform = %s", 
                           (new_username, platform_to_update))
            db.commit()
            print(f"Username for {platform_to_update} updated successfully.")
            
        else:
            print("Invalid choice. Please enter '1' or '2'.")
    else:
        print(f"No entry found for platform: {platform_to_update}")

# Main loop
while True:
    mode = input(f"\nWELCOME to password manager\n'view' to see all stored passwords \n'add' to add a new password  \n'delete' to delete a stored password \n'update' to update a password or username \n'q' to quit: \nENTER YOUR CHOICE: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view_passwords()
    elif mode == "add":
        add_password()
    elif mode == "delete":
        delete_password()
    elif mode == "update":
        update_password_or_username()
    else:
        print("Invalid mode")
        continue

cursor.close()
db.close()
