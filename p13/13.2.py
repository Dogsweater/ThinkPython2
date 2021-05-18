import random

def histogram(s):
    d=dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d

h=histogram('abbbc')
#print(h)

#练习13-5 按照频率的大小，成比例的随机返回一个值
#思路一：按照总量来编码：比如：5a,2b,3c 1-5->a,6-7->b,8-10->c

def reversedic(dict_normal):
    dict_reverse=dict()
    for keys,values in dict_normal.items():
        if values not in dict_reverse:
            dict_reverse[values]=[keys] #将它新建为一个列表
        else:
            dict_reverse[values].append(keys)#要让值是一个列表，而不是一个str
    return dict_reverse
    
def choose_from_hist(d):
    total=1
    #制作范围值
    for key in d:
        temp = d[key]
        d[key]=(range(total,d[key]+total))
        total+=temp
    #翻转字典
    newd=reversedic(d)
    r=random.randint(1,total-1)
    for key in newd:
        if r in key:
           letter=newd[key]
    return letter

random_letter=choose_from_hist(h)
print(random_letter)

'''
答案的解决
def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    # TODO: rewrite using Counter
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq)

    return random.choice(t)
'''