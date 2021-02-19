import math
l = []
N = 100
for a in range(2,N+1):
    for b in range(2,N+1):
        x = math.pow(a,b)
        if x not in l:
            l.append(x)
print(len(l))
