n = 10000000
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
        
def truncable(n):
    s = str(n)
    while(len(s)>1):
        s = s[:-1]
        x = int(s)
        if(prime[x]!=True):
            return False
    s = str(n)
    while(len(s)>1):
        s = s[1:]
        x = int(s)
        if(prime[x]!=True):
            return False
    return True
s = 0
for p in plist[4:]:
    if(truncable(p)):
        s += p
print(s)
