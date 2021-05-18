#联系10-1

def nested_sum(t):
    sum_=0
    for numlist in t:
        if(type(numlist)==list):
            sum_ =sum_+sum(numlist)
        elif(type(numlist)==int):
            sum_ += numlist
        else:
            return 'WRONG'
    return sum_

def cumsum(t):
    res=[]
    new_num=0
    for num in t:
        new_num +=num
        res.append(new_num)
    return res
    
#t=[3,[5,1],[4,1],'A']
#print(nested_sum(t))

t=[1,2,3]
print(cumsum(t))