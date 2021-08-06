def sieve(n):
    prime[0] = False
    prime[1] = False
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1


N = 2000000  # 2 million
prime = [True for i in range(N + 1)]
sieve(N)
sum_prime = 0
for p in range(N):
    if prime[p]:
        sum_prime += p

print(sum_prime)
