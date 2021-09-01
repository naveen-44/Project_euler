def fastPower(a,b):
    # calculates powers in O(Logn) time
    if a == 1 or b == 0:
        return 1
    if b == 1:
        return a
    # call a recursive function for the remaining half
    t = fastPower(a,b//2)
    res = t*t
    if b%2 == 1:
        res = res*a
    return res


number = fastPower(2,1000)
digitSum = 0
for s in str(number):
    digitSum += int(s)
print(digitSum)
