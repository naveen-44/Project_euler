def sieve(n):
    prime[0] = False
    prime[1] = False
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1


N = 1000000  # million
prime = [True for i in range(N + 1)]
sieve(N)


def triangle_num(n):
    return int(n * (n + 1) / 2)


def n_factors(n):
    factors = 1
    p = 2
    while n != 1:
        x = 0
        if prime[p]:
            while n % p == 0 and n > 1:
                x += 1
                n = int(n / p)
            factors *= (x + 1)
        p += 1
    return factors


max_factors = 0
for i in range(1, 100000):
    t = triangle_num(i)
    if n_factors(t) > 500:
        print(t)
        break

