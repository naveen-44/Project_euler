import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


N = 600851475143

for i in range(int(math.sqrt(N)), 2, -1):
    if N % i == 0:
        if is_prime(i):
            print(i)
            break
# comment
