n = 50000000
prime = [True for i in range(n+1)]
prime[0] = False
prime[1] = False
def SieveOfEratosthenes():
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
SieveOfEratosthenes()
plist = []
for i in range(n):
    if prime[i]:
        plist.append(i)
        
N = 100000000
count = 0
for i in range(len(plist)):
    for j in range(i,len(plist)):
        if plist[i]*plist[j] < N:
            count+=1
        else:
            break
print(count)
