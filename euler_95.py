import math
from time import time 
t = time()
def divsum(n):
    ans = 0
    if(prime[n]):
        return 1
    if(n==1):
        return 1
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i == 0):
            ans += i
            ans += n//i
    x = math.sqrt(n)
    if int(x) == x:
        ans-=x
    return int(ans) + 1

def amicable(n):
    count = 1
    l = [n]
    k = divsum(n)
    while(k not in l and k<1000000):
        l.append(k)
        k = divsum(k)
    if(k==n):
        return len(l)
    return 1

ans = 0
num = 0
for i in range(1,20000):
    n = amicable(i)
    if(n>ans):
        ans = n
        num = i
print(num)
print(time()-t)
