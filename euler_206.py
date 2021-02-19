n = 11213141516171819
n2 = 19293949596979899
x = int(math.sqrt(n)) + 2
while(x*x<n2):
    s = str(x*x)
    if(s[0]=='1' and s[2]=='2' and s[4]=='3' and s[6]=='4' and s[8]=='5' ):
        if(s[10]=='6' and s[12]=='7' and s[14]=='8'):
            print(x*10)
            break
    if(x%10 == 3):
        x+=4
    elif(x%10 == 7):
        x+=6
    else:
        x+=1
