# Password Manager with SQL and Encryption

## Overview
This project is a simple command-line-based password manager written in Python. It securely stores platform credentials (username and password) in an SQL database with encryption using the `cryptography` library. The program allows users to view, add, delete, and update credentials for different platforms.

## Features
- **Encryption**: Uses the `cryptography.fernet` library to encrypt passwords before storing them in the SQL database, ensuring secure data storage.
- **SQL Integration**: Credentials are stored in a MySQL database, making the data management more efficient and scalable.
- **CRUD Operations**: Supports viewing, adding, deleting, and updating passwords and usernames.

## Prerequisites

Before running the program, ensure you have the following installed:

- **Python 3.x**
- **MySQL Server**
- **Python packages**: `mysql-connector-python`, `cryptography`

You can install the required Python packages using pip:

```bash
pip install mysql-connector-python cryptography

## Sample Workflow

### Add a Password:
- Enter the platform name, username, and password when prompted. 
- The password is encrypted and stored in the database.

### View Passwords:
- Enter `view` to see a list of all stored platforms, usernames, and decrypted passwords.

### Update a Password or Username:
- Select `update` and choose whether to update the username or password for a specific platform.

### Delete a Password:
- Select `delete` and enter the platform name to remove its credentials from the database.

## Security

- The password manager uses **Fernet** symmetric encryption to ensure that passwords are stored securely.
- The encryption key is generated and stored in a local file (`key.key`) and is required to decrypt the passwords.
