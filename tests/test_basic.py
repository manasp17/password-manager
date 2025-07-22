import unittest
from crypto_utils import derive_key, encrypt, decrypt

class TestCryptoUtils(unittest.TestCase):
    def test_encrypt_decrypt_cycle(self):
        master_password = "testpassword"
        salt = b"1234567890abcdef"
        key = derive_key(master_password, salt)
        data = b"hello world"
        encrypted = encrypt(data, key)
        decrypted = decrypt(encrypted, key)
        self.assertEqual(decrypted, data)

if __name__ == "__main__":
    unittest.main()
