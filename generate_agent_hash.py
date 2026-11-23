"""
generate_agent_hash.py
----------------------
Run this script whenever you want to set a new agent password.
It will print the bcrypt hash to paste into your .env file.

Usage:
    python generate_agent_hash.py
"""
import bcrypt
import getpass

new_password = getpass.getpass("Enter new agent password: ")
hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
print(f"\nPaste this into your .env file as AGENT_PASSWORD_HASH:\n{hashed}")