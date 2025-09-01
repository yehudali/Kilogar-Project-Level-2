class Encryptor:
    def __init__(self,key:int):
        self.key=key
    def encrypt (self,data:str):
        encrypted = bytearray()
        for byte in data.encode():
            encrypted.append(byte^ self.key)
            return bytes(encrypted)

        def decrypt(self, data):
            decrypted = bytearray()
            for byte in data:
                decrypted.append(byte ^ self.key)
            return decrypted.decode()
        #קוד לדוגמא
enc = Encryptor(123)
text = "Hello World"
encrypted = enc.encrypt(text)
print("Encrypted:", encrypted)

decrypted = enc.decrypt(encrypted)
print("Decrypted:", decrypted)

