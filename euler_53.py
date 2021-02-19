def fact(n):
    if(n<=1):
        return 1
    return n*fact(n-1)

def ncr(n,r):
    return (fact(n)//(fact(n-r)*fact(r)))
    
N = 1000000
count = 0
for n in range(1,101):
    for r in range(1,n+1):
        if(ncr(n,r)>N):
            count+=1
print(count)
