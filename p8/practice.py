
def overturn(string):
    index=len(string)-1
    while index >=0:
        print(string[index])
        index=index-1

#overturn('hello_world')

#我滴鬼鬼这也太智能了吧！
def fun_for(string):
    for letter in string:
        print(letter)
      
#fun_for('so good')

def duckname(prefixes,suffix):
    for letter in prefixes:
        if(letter=='Q'or letter=='O'):
            print(letter+'u'+suffix)
        else:
            print(letter+suffix)
     
#duckname('JKLMNOQP','ack')

#print('hello_world'[:])

def find1(string,letter,origin,endpiont):
    if (origin>=endpiont or endpiont-1 >len(string)):
        print('wrong input!')
        return -1
    else:
        index=origin-1
        while index<endpiont-1:
            if(string[index]==letter):
                break
            index=index+1
        if(index<=endpiont-1 and (letter==string[index])):
            return 'we find'+" '"+letter+"' "+'at '+str(index+1)
        else:
            return 'we can`t find'+" '"+letter+"' "+'in '+string
 
#print(find('hello_world','l',1,8))

def find2(string,letter,origin,endpiont):
    if (origin>=endpiont or endpiont-1 >len(string)):
        return -1
    else:
        index=origin-1
        while index<endpiont-1:
            if(string[index]==letter):
                break
            index=index+1
        if(index<=endpiont-1 and (letter==string[index])):
            return index+1
        else:
            return 0
 
#print(find('hello_world','l',1,8))

def count1(string,goal):
    count=0
    for letter in string:
        if(letter==goal):
            count=count+1
    return count

#print(count1('abbaacaaa','a'))

def count2(string,goal):
    count=0
    index=0
    while(True):
        index=find2(string,goal,index+1,len(string)+1)
        if(index>0):
            count=count+1
        else:
            break
    return count
    
print(count2('abbaaca','a'))
    
        