t1 = 1
t2 = 2
t3 = t1 + t2
even_sum = 2
N = 4000000
while t3 < N:
    if t3 % 2 == 0:
        # print(t3)
        even_sum = even_sum + t3
    t1 = t2
    t2 = t3
    t3 = t1 + t2
print(even_sum)
