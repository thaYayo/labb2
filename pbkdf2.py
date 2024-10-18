import os
import hashlib

def pbkdf2_key_from_password():
    password = getpass("Ange lösenord: ").encode()
    hash_name = "sha256"
    salt = os.urandom(16)
    password_key = hashlib.pbkdf2_hmac(hash_name, password, salt, 200000)
    password_key = password_key.hex()
    return password_key
