import math

for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = math.sqrt(a*a + b*b)
        if c == int(c):
            if a+b+c == 1000:
                print(int(a * b * c))
                break
