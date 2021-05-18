#randint(a, b)
#——产生[a, b]之间的随机整数（其中a和b都可以取到，左闭右闭区间）

import random

def howmany_samebirthday(t):
    same_bir=0
    i=0
    while(i<len(t)-1):
        if t[i]==t[i+1]:
            same_bir +=2
            i+=2
        i=i+1
    probability=float(same_bir/len(t))
    return probability

#可以不用日期直接356天吧
def create_birday_list(num):
    res=[]
    for i in range(num):
        res.append(random.randint(1,356))
        res.sort()
    return res

def birthday_paradox(num_of_people, accuracy):
    sum_probability=0
    for i in range(accuracy):
        t=create_birday_list(num_of_people)
        sum_probability +=howmany_samebirthday(t)
    probability=float(sum_probability/accuracy)
    return probability

print(birthday_paradox(23,10000000))

git remote add origin https://github.com/Dogsweater/ThinkPython2.git
git branch -M main
git push -u origin main