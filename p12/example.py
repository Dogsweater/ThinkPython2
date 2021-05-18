'''
    字符串比其他序列有更多的限制，因为它的元素必须是字符，且不可变
    列表比元组更通用，主要是因为它是可变的。
    但有的时候使用元组更好：
    1.在返回语句中创建元组比创建列表从语法上来说更加简单
    2.如果需要用序列作为字典的键，则必须使用不可变类型，比如元组或字符串
    3.如果你要向函数传入一个序列作为参数，使用元组可能会减少潜在的不可知行为
    
    因为元组是不可变的，它们不提供sort和reverse之类的方法；
    但是Python也提供了内置函数sorted，可以接受任何序列作为参数，并按排行的顺序
    返回带有同样元素的列表，同样的还有reverse方法，它返回一个迭代器
'''

#可变长参数元组
def printall(*args):
	print (args)
	
printall(1,2.0,'3')

t=(7,3)
print(divmod(*t))

def sumall(*args):
    sum_all = 0
    for i in args:
        sum_all +=i
    return sum_all

print(sumall(7,5,4,2,1))

#zip

s='abcd'
t=[1,2,3,4]
zip(s,t)

for pair in zip(s,t):
    print(pair)
    
#用zip制作一个list

zip_list=list(zip(s,t))
print(zip_list)

#如果组合使用zip,for循环以及元组赋值，可以得到一种有用的模式，
#用于同时遍历两个或者更多序列

t1=(1,2,3,4)
t2=(2,1,3,4)
def has_macth(t1,t2):
    for x,y in zip(t1,t2):
        if x==y:
            return True
    return False

print(has_macth(t1,t2))

#如果需要遍历序列中的元素以及它们的下标，可以使用内置函数enumerate
for index ,element in enumerate ('abcd'):
    print(index,element)
    
#字典和元组
#字典有一个items方法可以返回一个元组的序列，其中每个元组是一个键值对：

d={'a':0,'b':1,'c':2}
t=d.items()
print(t)

#结果是一个dict_item对象，它是一个迭代器，可以迭代访问每一个键值对
#可以用for循环访问
for key,value in d.items():
    print(key,value)

#使用一个元组列表来初始化一个新的字典
t=('a',0),('c',2),('b',1)
d=dict(t)
print(d)

#组合使用dict和zip可以得到一个简洁的创建字典的方法：
d=dict(zip('abc',range(3)))
print(d)

#字典方法update也接受一个元组列表，并将它们作为键值对添加到一个已有的字典中
#以元组作为字典的键很常见
#directory[last,first]=number
directory=dict()
directory['Amy','Spears']=10086
directory['ack','Chen']=10000
directory['Mon','Jackson']=10087
for last,first in directory:
    print(first,last,directory[last,first])


