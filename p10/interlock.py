#啊这，忘了切片还有这种玩法了
#没有善用python自带的搜索包
def get_wordslist(fin):
    res=[]
    for line in fin:
        word=line.strip()
        res.append(word)
    return res

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

def binary_search(target,thelist):
    global flag
    global position
    while(len(thelist)>1):
        word=thelist[int(len(thelist)/2)]
        flag=if_before_macth(target,word)
        if(flag=='FOUND'):
            break
        elif(flag):
            binary_search(target,thelist[:int(len(thelist)/2)])
        else:
            binary_search(target,thelist[int(len(thelist)/2):])
        break
    if(flag=='FOUND'):
        return True
    return False


#把word打散在组合
#要分单数双数
def if_interlock(word,thelist):
    word_letter=list(word)
    i=0
    subword1=[]
    subword2=[]
    length=len(word_letter)
    while(i+1<length):
        subword1.append(word_letter[i])
        subword2.append(word_letter[i+1])
        i+=2
    if(length%2==1):
        subword1.append(word_letter[length-1])
    delimiter=''
    newword1=delimiter.join(subword1)
    newword2=delimiter.join(subword2)
    if(binary_search(newword1,thelist) and binary_search(newword2,thelist)):
        print(word)

def if_three_interlock(word,thelist):
    word_letter=list(word)
    i=0
    subword1=[]
    subword2=[]
    subword3=[]
    length=len(word_letter)
    while(i+2<length):
        subword1.append(word_letter[i])
        subword2.append(word_letter[i+1])
        subword2.append(word_letter[i+2])
        i+=3
    if(length%3==1):
        subword1.append(word_letter[length-1])
    elif(length%3==1):
        subword2.append(word_letter[length-2])
    delimiter=''
    newword1=delimiter.join(subword1)
    newword2=delimiter.join(subword2)
    newword3=delimiter.join(subword3)
    if(binary_search(newword1,thelist) and binary_search(newword2,thelist)and binary_search(newword3,thelist)):
        print(word)
        
def find_all(thelist):
    for word in thelist:
        if_interlock(word,thelist)
        
def find_three_all(thelist):
    for word in thelist:
        if_three_interlock(word,thelist)
    
flag=True
fin= open('f:/thinkpython2/p9/words.txt')
wordslist=get_wordslist(fin)
#if_interlock('aaaaaaa',wordslist)
#find_all(wordslist)
find_three_all(wordslist)