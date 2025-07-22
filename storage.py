import json, os
from crypto_utils import derive_key, encrypt, decrypt

VAULT_FILE = "data/vault.enc"
SALT_FILE  = "data/salt.bin"

def init_vault(master_password: str):
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(SALT_FILE):
        salt = os.urandom(16)
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
    else:
        with open(SALT_FILE, "rb") as f:
            salt = f.read()
    key = derive_key(master_password, salt)
    if not os.path.exists(VAULT_FILE):
        with open(VAULT_FILE, "wb") as f:
            f.write(encrypt(json.dumps({}).encode(), key))
    return key

def load_vault(key: bytes) -> dict:
    with open(VAULT_FILE, "rb") as f:
        data = f.read()
    return json.loads(decrypt(data, key))

def save_vault(vault: dict, key: bytes):
    with open(VAULT_FILE, "wb") as f:
        f.write(encrypt(json.dumps(vault).encode(), key))
