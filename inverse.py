import math

a = int(input("Enter a: "))
m = int(input("Enter modulus m: "))

if m <= 1:
    print("Modulus must be greater than 1.")
elif math.gcd(a, m) != 1:
    print("Multiplicative inverse does not exist.")
else:
    inverse = pow(a, -1, m)
    print("Multiplicative inverse =", inverse)
    print("Verification:", (a * inverse) % m, "= 1")
