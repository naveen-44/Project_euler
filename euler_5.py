import math


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


N = 20
ans = 1
for i in range(N+1):
    if is_prime(i):
        # print("i", i)
        x = i
        while x*i <= N:
            x = x * i
        # print("x", x)
        ans = ans * x
        
print(ans)
