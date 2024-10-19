# Nyckelgenerering:
# Skapa ett separat skript (ex: generate_key.py) som genererar en symmetrisk nyckel och sparar den i en fil.
import os
from cryptography.fernet import Fernet

def key_generator(output=None):
    key = Fernet.generate_key()
    if output:
        with open(f"{output}.key", "wb") as f:
            f.write(key)
            print(f"Nyckeln har sparats i {output}.key")
    else:
        with open("crypto.key", "wb") as key_file:
            key_file.write(key)
            print(f"Nyckeln har sparats i {os.getcwd()}\\crypto.key")
