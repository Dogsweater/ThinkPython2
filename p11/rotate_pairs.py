
def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res
    
def make_dict(fin):
    d=dict()
    for line in fin:
        word=line.strip()
        d[word]=1
    return d570

def make_list(fin):
    l=list()
    for line in fin:
        word=line.strip()
        l.append(word)
    return l
    
def find_pairs(l,d,n):
    for word in l:
        r_word=rotate_word(word,n)
        if(r_word in d):
            print(word,r_word,n)
    
fin=open('f:/thinkpython2/p9/words.txt')
d=make_dict(fin)
#为什么没有这行之后整个list什么也读不到，是fin空了吗
fin=open('f:/thinkpython2/p9/words.txt')
l=make_list(fin)
find_pairs(l,d,8)
