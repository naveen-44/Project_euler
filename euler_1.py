N = 999
d1, d2, d3 = 3, 5, 15
a1, a2, a3 = d1, d2, d3
n1, n2, n3 = int(N/d1), int(N/d2), int(N/d3)

s1 = int(n1/2*(2*a1 + (n1-1)*d1))
s2 = int(n2/2*(2*a2 + (n2-1)*d2))
s3 = int(n3/2*(2*a3 + (n3-1)*d3))

print(s1+s2-s3)
