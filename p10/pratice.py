#append()直接加在List后面，+新建列表，切片操作会新建一个列表-
word_list=['amendment','Vice','pointed','Span','Rival','spit','ABAC']
mix_list=[1,'dairy',2.0,False]
new_list=word_list[2:4]
word_list.append('slipup')

num_list=[1,2,3,4,5]
#print(sum(num_list))

def capitalize_all(t):
    res=[]
    for s in t:
        res.append(s.capitalize())
    return res

def only_upper(t):
    res=[]
    for s in t:
        if(s.isupper()):
            res.append(s)
    return res
    
#s=only_upper(word_list)
#del word_list[2:4]

new_word='pairie dairy starry'
t=new_word.split()
s='*'.join(t)

print(s)

'''
for word in t:
    print(word)
'''
