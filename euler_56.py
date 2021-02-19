ans = 0
for a in range(2,100):
    for b in range(2,100):
        x = a**b
        s = 0
        for i in str(x):
            s+=int(i)
        ans = max(s,ans)
print(ans)
