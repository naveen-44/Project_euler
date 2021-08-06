N = 300000
s = ''
for n in range(N):
    s = s + str(n)
print(int(s[1])*int(s[10])*int(s[100])*int(s[1000])*int(s[10000])*int(s[100000])*int(s[1000000]))
