import math

n = int(input("Enter the number of equations: "))

if n < 1:
    print("Enter at least one equation.")
else:
    remainders = []
    moduli = []

    for i in range(n):
        a = int(input(f"Enter remainder a{i + 1}: "))
        m = int(input(f"Enter modulus m{i + 1}: "))

        remainders.append(a)
        moduli.append(m)

    if any(m <= 1 for m in moduli):
        print("All moduli must be greater than 1.")
    elif any(
        math.gcd(moduli[i], moduli[j]) != 1
        for i in range(n)
        for j in range(i + 1, n)
    ):
        print("Moduli must be pairwise relatively prime.")
    else:
        M = math.prod(moduli)
        x = 0

        for a, m in zip(remainders, moduli):
            Mi = M // m
            inverse = pow(Mi, -1, m)
            x += a * Mi * inverse

        x %= M

        print("Smallest non-negative solution x =", x)
        print("Product of moduli =", M)
