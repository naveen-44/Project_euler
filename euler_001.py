# Sum of an arithmetic progession or AP 
# We find the sum of all the multiples of 3, 5 and 15 seperately
# Then we subract the sum of 15 from the sum of the sum of 3 and 5

def sumOfAP(a,d,n):
  return int(n/2*(2*a + (n-1)*d)) 


N = 999
d1, d2, d3 = 3, 5, 15               # Difference between each term of AP
a1, a2, a3 = 3, 5, 15               # Starting term of the AP
n1, n2, n3 = N//d1, N//d2, N//d3    # number of terms under 1000 as per question

s1 = sumOfAP(a1,d1,n1)              # sum of all the multiples of 3
s2 = sumOfAP(a2,d2,n2)              # sum of all the multiples of 5
s3 = sumOfAP(a3,d3,n3)              # sum of all the multiples of 15

print(s1+s2-s3)                     # required result
