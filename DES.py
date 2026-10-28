
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'8bytekey'
msg = input("Enter message: ").encode()

cipher = DES.new(key, DES.MODE_ECB)
encrypted = cipher.encrypt(pad(msg, 8))
print("Encrypted:", encrypted.hex())

decrypted = unpad(cipher.decrypt(encrypted), 8)
print("Decrypted:", decrypted.decode())
