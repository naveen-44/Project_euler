from time import time

cube_list = []
for i in range(1000000):
    cube_list.append(i*i*i)
    
def num_count(a):
    s = str(a)
    d = []
    for i in range(10):
        d.append(0)
    for i in s:
        d[int(i)]+=1
    return d

def is_perm(a,b):
    for i in range(10):
        if(a[i]!=b[i]):
            return False
    return True

num_count_list = []
for i in range(10000):
    num_count_list.append(num_count(cube_list[i]))

t = time()
score = []
perms = []

for x in range(10000):
    score.append(0)
    perms.append([])
    
flag = False
for i in range(10000):
    if(flag == True):
        break
    for j in range(i+1,10000):
        if(is_perm(num_count_list[i],num_count_list[j])):
            score[i]+=1
            perms[i].append(j)
            if(score[i]>=4):
                print(i,score[i],perms[i])
                print("answer = ",cube_list[i])
                print(time()-t)
                flag = True
                break
        if(sum(num_count_list[j])>sum(num_count_list[i])):
            break
