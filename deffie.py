


p = int(input("Enter prime number p: "))
g = int(input("Enter generator g: "))

a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))


A = pow(g, a, p)
B = pow(g, b, p)

print("Alice's public key:", A)
print("Bob's public key:", B)


alice_key = pow(B, a, p)
bob_key = pow(A, b, p)

print("Alice's shared key:", alice_key)
print("Bob's shared key:", bob_key)

if alice_key == bob_key:
    print("Key exchange successful!")
