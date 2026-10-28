a = int(input("Enter the dividend (a): "))
b = int(input("Enter the divisor (b): "))

if b == 0:
    print("Error: Divisor cannot be zero.")
else:
    q = a // abs(b)
    r = a % abs(b)

    
    if b < 0:
        q = -q

    print("Dividend (a):", a)
    print("Divisor (b):", b)
    print("Quotient (q):", q)
    print("Remainder (r):", r)
    print("Verification: a = b*q + r")
    print("Result:", b * q + r)
