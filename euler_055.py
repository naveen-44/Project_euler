def rev(n):
    s = str(n)
    s1 = s[::-1]
    return int(s1)

def ispal(n):
    s = str(n)
    s1 = s[::-1]
    if(s == s1):
        return True
    return False

def lychrel(n):
    c = 1
    n = n + rev(n)
    while(ispal(n)==False and c<51):
        n = n + rev(n)
        c+=1
    if(c>50):
        return True
    return False

count = 0
for i in range(1,10000):
    if(lychrel(i)):
        count+=1
print(count)
