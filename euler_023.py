import math
def checkAbundant(number):
    divSum = 1
    for n in range(2,int(math.sqrt(number))+1):
        if number%n==0:
            divSum+=n
            divSum+=(number//n)
    if int(math.sqrt(number))**2 == number:
        divSum -= math.sqrt(number)
    return divSum>number

def makeAbundantListTill(number = 28123):
    abundantList = []
    for i in range(1,number+1):
        if checkAbundant(i):
            abundantList.append(i)
    return abundantList

def findAllNumbers(number):
    # find numbers that can be expressed as sum of
    # any two abundant numbers (including repetitive)
    nums = [False for i in range(number + 1)]
    for i in range(len(abundantList)):
        for j in range(i,len(abundantList)):
            n = abundantList[i]+abundantList[j]
            if n>28123:
                break
            else:
                nums[n]=True

number = 28123
result = 0
abundantList = makeAbundantListTill()
findAllNumbers(number)
for i in range(number+1):
    if not nums[i]:
        result+=i
print(result)
