def factorial(n):
    if n <= 1:
        return 1
    return factorial(n-1)*n


N = 100
a = factorial(N)
a = str(a)
res = 0
for d in a:
    res = int(d) + res
print(res)
