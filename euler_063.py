def power(a,b):
    ans = 1
    for i in range(b):
        ans = ans * a
    return ans

ans = []
for a in range(1,100):
    for b in range(1,100):
        s = str(power(a,b))
        if(len(s)==b):
#             print(a,b,s)
            if(int(s) not in ans):
                ans.append(int(s))
print(len(ans))
