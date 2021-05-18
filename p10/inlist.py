
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
            position+=int(len(thelist)/2)
            break
        elif(flag):
            binary_search(target,thelist[:int(len(thelist)/2)])
        else:
            position+=int(len(thelist)/2)
            binary_search(target,thelist[int(len(thelist)/2):])
        break
    if(flag=='FOUND'):
        return position+1
    return "target word not in wordslist"

#leavier
position=0
flag=True
fin= open('f:/thinkpython2/p9/words.txt')
wordslist=get_wordslist(fin)
print(binary_search('lair',wordslist))
print(binary_search('eve',wordslist))