def is_palindrome(n):
    # returns a bool true if given number is a palindrome
    # else returns false
    
    string1 = str(n)            # converts the number to string
    string2 = string1[::-1]     # reverses the string and compares
    if string1 == string2:
        return True
    return False

ans = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        x = i*j
        if is_palindrome(x):
            if x > ans:         # checks if larger and updates
                ans = x

print(ans)
