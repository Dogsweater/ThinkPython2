#对比我写的来看，简单很多
#原因是我执着与用find函数和没有属性Python的语法

def has_no_e(word):
    for letter in word:
        if letter=='e'
            return False
    return True

#python也太聪明了吧，呜呜呜
def avoids(word,forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

#python也太聪明了,并且我可能没有搞清楚在一个函数中return之后就直接退出了，不用花里胡哨
def uses_only(word,available):
    for letter in word:
        if letter not in  available:
            return False
    return True
    
