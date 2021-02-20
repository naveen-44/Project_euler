N = 10
nn = 10
count = []
pcount = 0
for n in range(10**8 + 1):
    r = rev(n)
    x = n + r
    s = str(x)
    flag = True
    for i in s:
        if(int(i)%2==0):
            flag = False
            break
    if(flag == True and n%10>0 and r%10>0):
        pcount+=1
    if(n==N):
        count.append(pcount)
#         print(N,pcount,sum(count))
        N = N*10
        pcount = 0
print(sum(count))
