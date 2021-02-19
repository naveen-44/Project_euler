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
print(len(plist))


def samenums(n1,n2):
    s1,s2 = str(n1), str(n2)
    a1 = [0 for i in range(10)]
    a2 = [0 for i in range(10)]
    for s in s1:
        a1[int(s)]+=1
    for s in s2:
        a2[int(s)]+=1
    for i in range(10):
        if(a1[i]!=a2[i]):
            return False
    return True

for i in range(168,1229):
    p1 = plist[i]
    for j in range(i+1,1229):
        p2 = plist[j]
        if(samenums(p1,p2)):
            for k in range(j+1,1229):
                p3 = plist[k]
                if(p3-p2 == p2-p1):
                    if(samenums(p2,p3)):
                        print(str(p1)+str(p2)+str(p3))
