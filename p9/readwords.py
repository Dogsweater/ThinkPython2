
def find_long(fin):
    for line in fin:
        word=line.strip()
        if(len(word)>20):
            print(word)

def has_no_e(fin):
    counter=0
    counter_e=0
    for line in fin:
        word=line.strip()
        counter=counter+1
        if(word.find('e')==-1):
            counter_e=counter_e+1
    return (float(counter_e/counter))

def avoids(word,letter):
    if(word.find(letter)==-1):
        return True
    else:
        return False
    
def find_avoids():
    counter=0
    letters=input('please enter the 5 letters you wanan to avoid ')
    fin=open('f:/thinkpython2/p9/words.txt')
    for line in fin:
        word=line.strip()
        flag=False
        for letter in letters:
            if(word.find(letter)==-1):
                flag=True
            else:
                flag=False
                break
        if(flag==True):
            print(word)
            counter=counter+1
    print(counter)

def uses_only(word,sub):
    outflag = True
    for c in word:
        flag = False
        for letter in sub:
            if(c==letter):
                flag=True
                break
        if flag==False:
            outflag = False
            break
    if outflag==True:
        return ('it right!')
    else:
        return ('it wrong')

def is_abeccedarain(word):
    last_letter='a'
    for letter in word:
        if(letter<last_letter):
            flag=False
            return False
        last_letter=letter
    return True


def howmuch_abeccedarain():
    counter=0
    fin=open('f:/thinkpython2/p9/words.txt')
    for line in fin:
        word=line.strip()
        if(is_abeccedarain(word)==True):
            print(word)
            counter=counter+1
    print(counter)

    
fin=open('f:/thinkpython2/p9/words.txt')
#find_long(fin)
#print(has_no_e(fin))
#print(avoids('abcdf','ad'))
#find_avoids()
#print(uses_only('aabbcdc','acb'))
print(is_abeccedarain('abcdeffgh'))