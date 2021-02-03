def is_pal(n):
    s1 = str(n)
    s2 = s1[::-1]
    if s1 == s2:
        return True
    return False


ans = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        x = i*j
        if is_pal(x):
            if x > ans:
                ans = x

print(ans)
