def collatz(n):
    c = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3*n + 1)
        c += 1
    return c


ans = 0
length = 0
N = 1000000     # million
for i in range(77031, N):
    t = collatz(i)
    if t > length:
        length = t
        ans = i

print(ans)
