13import math

n = int(input("Enter a positive integer: "))

if n < 1:
    print("Enter a positive integer.")
else:
    count = 0

    for i in range(1, n + 1):
        if math.gcd(i, n) == 1:
            count += 1

    print("Euler's Totient Function =", count)
