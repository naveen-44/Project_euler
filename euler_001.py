# Sum of an arithmetic progession or AP 
# We find the sum of all the multiples of 3, 5 and 15 seperately
# Then we subract the sum of 15 from the sum of the sum of 3 and 5

N = 999
d1, d2, d3 = 3, 5, 15                         # Difference between each term of AP
a1, a2, a3 = 3, 5, 15                         # Starting term of the AP
n1, n2, n3 = int(N/d1), int(N/d2), int(N/d3)  # number of terms under 1000 as per question

s1 = int(n1/2*(2*a1 + (n1-1)*d1))             # sum of all the multiples of 3
s2 = int(n2/2*(2*a2 + (n2-1)*d2))             # sum of all the multiples of 5
s3 = int(n3/2*(2*a3 + (n3-1)*d3))             # sum of all the multiples of 15

print(s1+s2-s3)                               # requires result
