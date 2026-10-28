import math

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if math.gcd(a, b) == 1:
    print(a, "and", b, "are relatively prime.")
else:
    print(a, "and", b, "are not relatively prime.")

print("GCD =", math.gcd(a, b))
