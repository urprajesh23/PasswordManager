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

