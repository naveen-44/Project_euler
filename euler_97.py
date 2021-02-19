a = 2
b = 7830457
x = 28433
m = 10**10
n = 1
for i in range(b):
    n = n * 2
    n = n % m

n = n * x
n = n % m
n = n + 1

print(n)
