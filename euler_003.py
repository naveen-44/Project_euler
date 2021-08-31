import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def largestPrimeFactor(N):
    for i in range(int(math.sqrt(N)), 1, -1):
        if N % i == 0:
            if is_prime(i):
                return i
            
N = 600851475143
print(largestPrimeFactor(N))
