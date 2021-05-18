'''
好多自带的函数没有用，数据结构的选择也有待提高
字典中有很多优秀的方法
'''
#用 for in punctucation来判断是不是特殊字符
import string

#13-1 读入文件大写字母转换为小写，把非字母之外的东西剥除

#有一个问题叫做:string是不是不能改变，是不是每次都新建了一个，占内存
def clean_string():
    fin =open('haripot.txt')
    cleanstring=''
    for line in fin:
        for letter in line:
            if (letter not in string.punctuation) and (letter not in string.whitespace):
                if(64<ord(letter)<97 ):
                    letter=chr(ord(letter)+32)
                cleanstring=cleanstring+letter
    return cleanstring
                
#练习13-2 不会文件读取，做这个好麻烦
#去除信息部分，思路是读行到那个地方
#抄一下跳过开头的代码

def skip_header(fin):
    for line in fin:
        if line.startswith('*** START OF THIS'):
            break
          
def get_right_text(fin,if_skip):
    text=list()
    if(if_skip):
        skip_header(fin)
    for line in fin:
        if line.startswith('*** END OF THIS'):
            break
        #for word in line:  #打印的为什么是letter
        sentence=line.strip()
        clean_sentence=''
        for letter in sentence:
            if letter not in (string.whitespace and string.punctuation):
                if(64<ord(letter)<97 ):
                    letter=chr(ord(letter)+32)
                clean_sentence+=letter    
        #text.append(clean_sentence.split())#啊这，加的是元组
        text+=(clean_sentence.split())
    return text
 
word_total=0 
def make_dict(t):
    d={}
    global word_total
    for word in text:
        if word not in d:
            d[word]=1
            word_total+=1
        else:
            d[word]+=1
    return d
     
fin =open('514.txt')    
text=get_right_text(fin,True)
#d=make_dict(text)
#print(word_total)
#print(d)

#练习13-2
#统计使用频率最高的20个单词
#思路一：翻转字典，排序列表，前20项
#找到二十个大值 一个值的数组？

def get_most_frequse(d):
    max_times=[[0,'a']]*20
    for key in d:
        word=key
        times=d[key]
        i=0
        while(i<20):#为什么数据不进去
            if max_times[i][0]<times:
                max_times[i]=[times,word]
                max_times.sort()
                break
            i+=1
    max_times.reverse()
    index=0
    for times,word in max_times:
        index+=1
        print(index,word)
    return True
            
        
#get_most_frequse(d)
 
#练习13-4 寻找没有在单词表里的单词：
def make_word_list():
    wordlist=list()
    fin=open('F:/thinkpython2/p9/words.txt')
    for line in fin:
        word=line.strip()
        wordlist.append(word)
    return wordlist

#去除重复的单词
def once_word(l):
    newl=list()
    for word in l:
        if word not in newl:
            newl.append(word)
    return newl
        
        
def find_not_in_list(useword,wordlist):
    for word in useword:
        if word not in wordlist:
            print(word)

l=make_word_list()
newtext=once_word(text)
find_not_in_list(newtext,l)