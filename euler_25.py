t1 = 1
t2 = 1
t3 = t2 + t1
n = 3

while len(str(t3)) < 1000:
    t1, t2, t3 = t2, t3, t2 + t3
    n += 1

print(n)