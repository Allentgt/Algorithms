'''Find the first n prime numbers'''

def gen_prime(n):
    primes = [True for i in range(n)]
    p = 2
    while (p**2 <= n):
        for i in range(p*2, n, p):
            primes[i] = False
        p += 1

    for i in range(2,len(primes)):
        if primes[i]:
            print i

gen_prime(300)

