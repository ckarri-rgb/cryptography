a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
m = int(input("Enter the modulus (m): "))

if m <= 0:
    print("Error: Modulus must be positive.")
else:
    print("Addition:", (a + b) % m)
    print("Subtraction:", (a - b) % m)
    print("Multiplication:", (a * b) % m)

    print("a mod m =", a % m)
    print("b mod m =", b % m)

    if b % m != 0:
        print("Division is not always defined in modular arithmetic.")
        if __import__("math").gcd(b, m) == 1:
            inverse = pow(b, -1, m)
            print("Modular inverse of b:", inverse)
            print("a / b mod m =", (a * inverse) % m)
        else:
            print("b has no modular inverse modulo m.")
