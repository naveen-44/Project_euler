def sieve(n):
    prime[0] = False
    prime[1] = False
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1


N = 200000
prime = [True for i in range(N + 1)]
sieve(N)
counter = 0
for p in range(N):
    if prime[p]:
        counter += 1
    if counter == 10001:
        print(p)
        break
