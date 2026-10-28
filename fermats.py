
a = int(input("Enter a: "))
p = int(input("Enter a prime number p: "))

if p <= 1:
    print("p must be greater than 1.")
else:
    is_prime = all(p % i != 0 for i in range(2, int(p**0.5) + 1))

    if not is_prime:
        print("p must be prime.")
    elif a % p == 0:
        print("The theorem requires a not divisible by p.")
    else:
        result = pow(a, p - 1, p)
        print("a^(p-1) mod p =", result)
        print("Fermat's Little Theorem verified:",
              result == 1)
