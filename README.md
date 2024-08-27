# Password Manager with SQL and Encryption

## Overview
This project is a simple command-line-based password manager written in Python. It securely stores platform credentials (username and password) in an SQL database with encryption using the `cryptography` library. The program allows users to view, add, delete, and update credentials for different platforms.

## Features
- **Encryption**: Uses the `cryptography.fernet` library to encrypt passwords before storing them in the SQL database, ensuring secure data storage.
- **SQL Integration**: Credentials are stored in a MySQL database, making the data management more efficient and scalable.
- **CRUD Operations**: Supports viewing, adding, deleting, and updating passwords and usernames.

