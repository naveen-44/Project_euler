def pandigital(s):
    if(len(s)!=9):
        return False
    x = [0 for i in range(10)]
    for i in s:
        i = int(i)
        x[i]+=1
    if(x[0]>0):
        return False
    for i in x[1:]:
        if(i!=1):
            return False
    return True

sum1 = []
for i in range(8000):
    for j in range(i,8000):
        x = i*j
        s = str(i)+str(j)+str(x)
        if(pandigital(s)):
            if(x not in sum1):
                sum1.append(x)
        if(len(s)>9):
            break
print(sum(sum1))
