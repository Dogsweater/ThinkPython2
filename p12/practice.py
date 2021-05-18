#12-1
import string

def reversedic(dict_normal):
    dict_reverse=dict()
    for keys,values in dict_normal.items():
        if values not in dict_reverse:
            dict_reverse[values]=[keys] #将它新建为一个列表
        else:
            dict_reverse[values].append(keys)#要让值是一个列表，而不是一个str
    return dict_reverse
    
def most_frequent(string):
    word = list(string)
    letterbook=dict()
    for letter in word:
        if letter not in letterbook:
            letterbook[letter]=1
        else:
            letterbook[letter]+=1
    #翻转字典
    newletterbook=reversedic(letterbook)
    #将字典转换为排列好的list
    letterlist=sorted(newletterbook.items(),reverse=True)
    #把数量取出
    newletterlist=list()
    for t in letterlist:
        newletterlist.append(t[1])
    return newletterlist
 
'''
参考了参考代码的读取文件
'''
def file_to_sting():
    string=open('haripot.txt').read()
    return string

def clean_string():
    fin =open('215.txt')
    cleanstring=''
    for line in fin:
        for letter in line:
            if (letter not in string.punctuation) and (letter not in string.whitespace):
                if(64<ord(letter)<97):
                    letter=chr(ord(letter)+32)
                cleanstring=cleanstring+letter
    return cleanstring
                
english_text=clean_string() 
#print(english_text)
print(most_frequent(english_text))
#d={'a':1,'b':2,'d':4,'c':3,'e':3}
#print(reversedic(d))   