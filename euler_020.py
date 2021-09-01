def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)
    
digitSum = 0
for s in str(fact(100)):
    digitSum += int(s)
print(digitSum)
