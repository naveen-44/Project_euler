n = 1000000
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

def iscircularprime(n):
    if n < 10 and prime[n]:
        return True
    s = str(n)
    s1 = s[1:] + s[0]
    while(int(s1)!=n):
        if(prime[int(s1)]!=True):
            return False
        s1 = s[1:] + s[0]
        s = s1
    return True

count = 0
for p in plist:
    if(iscircularprime(p)):
        count+=1
print(count)
