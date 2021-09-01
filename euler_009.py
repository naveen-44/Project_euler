import math

flag = False
for a in range(1, 1000):
    if not flag:                        # found answer or not
        for b in range(a+1, 1000):
            c = math.sqrt(a*a + b*b)    
            if a+b+c >1000:             # no need to loop further
                break
            if a+b+c == 1000:           # no need to run further coz only one solution
                print(int(a*b*c))
                flag = True
