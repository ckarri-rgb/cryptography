

def rc4(key, data):
    S = list(range(256))
    j = 0

    
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    
    i = j = 0
    result = []

    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        result.append(byte ^ k)

    return bytes(result)


key = input("Enter key: ").encode()
message = input("Enter message: ").encode()

if not key:
    print("Key cannot be empty.")
else:
    encrypted = rc4(key, message)
    print("Encrypted:", encrypted.hex())

    decrypted = rc4(key, encrypted)
    print("Decrypted:", decrypted.decode())
