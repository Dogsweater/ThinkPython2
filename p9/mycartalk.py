#练习9-7
#有一说一，我这个递归解法挺漂亮的，感觉比答案带劲
def is_three_pairs(word):
    if len(word)<6:
        return False
    if word[0]==word[1]:
        if word[2]==word[3]:
            if word[4]==word[5]:
                return True
    return is_three_pairs(word[1:])

def find_in_list(fin):
    counter=0
    for line in fin:
        word=line.strip()
        if(is_three_pairs(word)):
            print(word)
            counter=counter+1
    print(counter) 

#fin=open('f:/thinkpython2/p9/words.txt')
#find_in_list(fin)

#练习9-8
def is_palindrome(word):
    i=0
    j=len(word)-1
    while(i<j):
        if(word[i]!=word[j]):
            return False
        i=i+1
        j=j-1
    return True

#少了一个解，是切片操作的时候错了，切片后面的数字不在切片中 
#答案的解比我漂亮非常多       
def plex2():
    i=100000
    while(i<1000000):
        string=str(i)
        if (is_palindrome(string[2:])):
            string=str(i+1)
            if(is_palindrome(string[1:])):
                string=str(i+2)
                if(is_palindrome(string[1:5])):
                     string=str(i+3)
                     if(is_palindrome(string)):
                        print(i)
        i=i+1
        
plex2()

#练习9-9

def two_char_reverse(string):
    if(len(string)!=2):
        return False
    new_string=string[1]+string[0]
    return new_string

#有点丑=-=，不知道怎么找第六个 
#函数比我写的好看
#而且这是我没想到的
# assuming that mother and daughter don't have the same birthday,
# they have two chances per year to have palindromic ages.
def plex3():
    for distance in range(50):
        counter=0
        for i in range(100-distance):
            me=i
            mom=me+distance
            if(two_char_reverse(str(me).zfill(2))==str(mom)):
                counter=counter+1
        if(counter==8):
            flag=1
            for i in range(100-distance):
                me=i
                mom=me+distance
                if(two_char_reverse(str(me).zfill(2))==str(mom)):
                    flag=flag+1
                    if(flag==6):
                        print(me)
                        return
#plex3()
               
            
        
