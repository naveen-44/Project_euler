import math
n = 1000
p = int(math.pow(2, n))
p = str(p)

res = 0
for d in p:
    res = int(d) + res

print(res)
