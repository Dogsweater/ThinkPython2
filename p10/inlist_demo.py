#匹配：先做长度测试：长度一致才可能匹配
#当首字母匹配时，对第二个字母是否需要二分查找？
#递归：不匹配截断wordslist，匹配截断word
#严重问题：递归怎么把返回值一直传递
#虽然看上去有点丑陋，但是呜呜呜，搞定了！
def get_wordslist(fin):
    res=[]
    for line in fin:
        word=line.strip()
        res.append(word)
    return res

#接受字母，判断单词位置，返回Bool
#总感觉有问题，怎么让递归停止？
#如果是一部分呢？ acdd 和 acd
#原来是你这个遭老头子错了，测试不完全，用例少了
def if_before_macth(target,word):
    if(target==word):
        return 'FOUND'
    i=0
    while(i<len(target) and i<len(word)):
        if((target[i])<word[i]):
            return True
        elif((target[i])>word[i]):
            return False
        i+=1
    if(len(target)<len(word)):
        return True
    return False

#判断，返回位置
#注意会不会有值一直没有取到

#问题：没找到单词时不会退出，找到了也不会
#向上层return时怎么退出
#呜呜呜，这个break伤了我太多
#找到的位置怎么返回
#！！这个return没有用，它还是执行了17次

position=0
flag=True
    
def binary_search(target,thelist):
    global flag
    global position
    while(len(thelist)>1):
        word=thelist[int(len(thelist)/2)]
        flag=if_before_macth(target,word)
        if(flag=='FOUND'):
            position+=int(len(thelist)/2)
            break
        elif(flag):
            binary_search(target,thelist[:int(len(thelist)/2)])
        else:
            position+=int(len(thelist)/2)
            binary_search(target,thelist[int(len(thelist)/2):])
        break
    if(flag=='FOUND'):
        #为什么这玩意要执行这么多次，能不能直接传到最外层函数
        #print('here')
        return position+1
    return "target word not in wordslist"
    
    

fin= open('f:/thinkpython2/p9/words.txt')
wordslist=get_wordslist(fin)
print(binary_search('trudge',wordslist))
#print(if_before_macth('longshore','aggressed'))