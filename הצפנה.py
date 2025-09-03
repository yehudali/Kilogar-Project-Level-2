
import random

# מפתח אקראי של אורך 8 בתיםv u
key = bytes([random.randint(0, 255) for _ in range(8)])
print("Random key:", key)
class Encryptor:
    def __init__(self, key: bytes = None):
        if key is None:
            # אם לא הוזן מפתח, נוציא מפתח אקראי באורך 8 בתים
            key = bytes([random.randint(0, 255) for _ in range(8)])
        self.key = key

    def encrypt(self, data: str) -> bytes:
        encrypted = bytearray()
        key_len = len(self.key)
        for i, byte in enumerate(data.encode()):
            encrypted.append(byte ^ self.key[i % key_len])
        return bytes(encrypted)

    def decrypt(self, data: bytes) -> str:
        decrypted = bytearray()
        key_len = len(self.key)
        for i, byte in enumerate(data):
            decrypted.append(byte ^ self.key[i % key_len])
        return decrypted.decode(errors="ignore")

