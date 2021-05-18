#没有考虑好ACSII码，完成度不够
def rotate_word(secret,num):
    for c in secret:
        new_n=ord(c)+num
        if (new_n-ord('z')>0):
            new_n=new_n-26
        new_c=chr(new_n)
        print(new_c,end='')

rotate_word("CMS",-10)