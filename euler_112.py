def inc(n):
    s = str(n)
    for i in range(len(s)-1):
        if s[i]>s[i+1]:
            return False
    return True

def dec(n):
    s = str(n)
    for i in range(len(s)-1):
        if s[i]<s[i+1]:
            return False
    return True

def isbouncy(n):
    if(inc(n) or dec(n)):
        return False
    return True
 
c = 0
for i in range(1,10000000):
    if(isbouncy(i)):
        c += 1
    p = c/i
    if(p==0.99):
        print(i,c,p)
        break
