
#解法1 表,也快，因为存了数字
def fibonacci(times):
    sequence=[0,1]
    i = 2
    while(i<=times):
        new_num = sequence[i-2]+sequence[i-1]
        sequence.append(new_num)
        i+=1
    return sequence

#解法2 求数
def fibonacci2(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci2(n-1)+fibonacci2(n-2)

#print(fibonacci2(40))

#解法3，制作memo

known={0:0,1:1}

#为什么只存了当前查询的，因为我递归的时候用的函数2，什么狗问题啊！
def fibonacci3(n):
    if n in known:
        return known[n]
        
    res=fibonacci3(n-1)+fibonacci3(n-2)
    known[n]=res
    return res
    
print(fibonacci3(40))
print(known)