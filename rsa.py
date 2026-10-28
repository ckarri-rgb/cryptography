

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


key = RSA.generate(2048)
public_key = key.publickey()

message = input("Enter message: ").encode()


encryptor = PKCS1_OAEP.new(public_key)
encrypted = encryptor.encrypt(message)
print("Encrypted:", encrypted.hex())

decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(encrypted)
print("Decrypted:", decrypted.decode())
