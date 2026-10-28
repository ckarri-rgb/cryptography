def encrypt(msg, n):
    return ''.join(msg[i::n] for i in range(n))

def decrypt(ct, n):
    rows = [len(range(i, len(ct), n)) for i in range(n)]
    cols, k = [], 0
    for size in rows:
        cols.append(ct[k:k+size])
        k += size
    return ''.join(cols[i][j]
                   for j in range(max(rows))
                   for i in range(n) if j < rows[i])

msg = input("Message: ")
n = int(input("Rails: "))
ct = encrypt(msg, n)
print("Encrypted:", ct)
print("Decrypted:", decrypt(ct, n))