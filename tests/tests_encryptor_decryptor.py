import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cryptography.fernet import Fernet
from utils.encryptor_decryptor import (
    encrypt_fernet,
    decrypt_fernet,
    encrypt_blowfish,
    decrypt_blowfish,
    encrypt_aes,
    decrypt_aes,
    generate_keys
)

class TestEncryptionDecryption(unittest.TestCase):
    def setUp(self):
        # Generate keys for each encryption method
        self.fernet_key, self.blowfish_key, self.aes_key = generate_keys()
        self.password = "test_password_123"

    # Test for Fernet encryption and decryption
    def test_fernet_encrypt_decrypt(self):
        encrypted_password = encrypt_fernet(self.password, self.fernet_key)
        decrypted_password = decrypt_fernet(encrypted_password, self.fernet_key)
        self.assertEqual(self.password, decrypted_password)

    # Test for Blowfish encryption and decryption
    def test_blowfish_encrypt_decrypt(self):
        encrypted_password = encrypt_blowfish(self.password, self.blowfish_key)
        decrypted_password = decrypt_blowfish(encrypted_password, self.blowfish_key)
        self.assertEqual(self.password, decrypted_password)

    # Test for AES encryption and decryption
    def test_aes_encrypt_decrypt(self):
        encrypted_password = encrypt_aes(self.password, self.aes_key)
        decrypted_password = decrypt_aes(encrypted_password, self.aes_key)
        self.assertEqual(self.password, decrypted_password)

    # Test invalid Fernet decryption (e.g., incorrect key)
    def test_invalid_fernet_decrypt(self):
        invalid_key = Fernet.generate_key()  # Different key
        encrypted_password = encrypt_fernet(self.password, self.fernet_key)
        with self.assertRaises(Exception):
            decrypt_fernet(encrypted_password, invalid_key)

    # Test invalid Blowfish decryption (e.g., incorrect key)
    def test_invalid_blowfish_decrypt(self):
        invalid_key = os.urandom(16)  # Different key
        encrypted_password = encrypt_blowfish(self.password, self.blowfish_key)
        with self.assertRaises(Exception):
            decrypt_blowfish(encrypted_password, invalid_key)

    # Test invalid AES decryption (e.g., incorrect key)
    def test_invalid_aes_decrypt(self):
        invalid_key = os.urandom(16)  # Different key
        encrypted_password = encrypt_aes(self.password, self.aes_key)
        with self.assertRaises(Exception):
            decrypt_aes(encrypted_password, invalid_key)

if __name__ == '__main__':
    unittest.main()
