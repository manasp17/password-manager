from cryptography.fernet import Fernet
import base64, os
from hashlib import pbkdf2_hmac

def derive_key(master_password: str, salt: bytes) -> bytes:
    # derive a 32-byte key from master password
    kdf = pbkdf2_hmac('sha256', master_password.encode(), salt, 100_000, dklen=32)
    return base64.urlsafe_b64encode(kdf)

def encrypt(data: bytes, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(data)

def decrypt(data: bytes, key: bytes) -> bytes:
    f = Fernet(key)
    return f.decrypt(data)
