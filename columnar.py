def encrypt(msg, key):
    return ''.join(msg[i::len(key)]
                   for i in sorted(range(len(key)),
                                   key=lambda x: (key[x], x)))

def decrypt(ct, key):
    n, k = len(key), len(ct)
    sizes = [len(range(i, k, n)) for i in range(n)]
    cols, p = [''] * n, 0
    for i in sorted(range(n), key=lambda x: (key[x], x)):
        cols[i], p = ct[p:p+sizes[i]], p+sizes[i]
    return ''.join(cols[i][j]
                   for j in range(max(sizes))
                   for i in range(n) if j < sizes[i])

msg = input("Message (no spaces): ")
key = input("Keyword: ").upper()
ct = encrypt(msg, key)
print("Encrypted:", ct)
print("Decrypted:", decrypt(ct, key))