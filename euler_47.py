def sieve(n):
    prime[0] = False
    prime[1] = False
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1


def prime_list(n):
    plist = []
    for i in range(n+1):
        if prime[i]:
            plist.append(i)
    return plist


def prime_divisors_list(n, p_list):
    d_list = []
    i = 0
    while n > 1:
        p = p_list[i]
        i += 1
        while n % p == 0:
            n /= p
            if p not in d_list:
                d_list.append(p)
                if len(d_list) > 4:
                    return d_list
    return d_list


N = 1000000
prime = [True for i in range(N + 1)]
sieve(N)
plist = prime_list(N)
d_n = []
for i in range(N):
    if prime[i]:
        d_n.append([1, i])
    else:
        d_n.append(prime_divisors_list(i, plist))

for i in range(len(d_n)-3):
    if len(d_n[i]) == 4 and len(d_n[i+1]) == 4 and len(d_n[i+2]) == 4 and len(d_n[i+3]) == 4:
        print(i)
        break
