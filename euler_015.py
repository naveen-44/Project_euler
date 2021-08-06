def factorial(n):
    if n <= 1:
        return 1
    return factorial(n-1)*n


def ncr(n,r):
    return int(factorial(n)/(factorial(n-r)*factorial(r)))

N = 20

print(ncr(2*N, N))
