
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567890123456'
msg = input("Enter message: ").encode()

cipher = AES.new(key, AES.MODE_ECB)
encrypted = cipher.encrypt(pad(msg, 16))
print("Encrypted:", encrypted.hex())

decrypted = unpad(cipher.decrypt(encrypted), 16)
print("Decrypted:", decrypted.decode())
