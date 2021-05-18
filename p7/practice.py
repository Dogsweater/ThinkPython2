import math
#用循环而非递归的方式重写5.8中pirnt_n
def print_n(num,times):
    while(times>0):
        print(num)
        times=times-1
        
#练习7-1
#打印表格那里是完美啊
def square_root(a):
    x=5
    epsilon=0.00000001
    while(True):
        y=float((x+(a/x))/2)
        if(abs(y-x)<epsilon):
            break
        x=y
      
    return y

def test_square_root():
    i=1.0
    print ('a',' '*5,'mysqrt(a)',' '*15,'math.sqrt(a)',' '*15,'diff')
    print('-'*80)
    while(i<=15.0):
        mysq=square_root(i)
        sq=math.sqrt(i)
        diff=(abs(mysq-sq))
        n0=len('a'+' '*5)-len(str(i))
        n1=len('mysqrt(a)'+' '*15)-len(str(mysq))
        n2=len('math.sqrt(a)'+' '*15)-len(str(sq))
        print (i,' '*n0,mysq,' '*n1,sq,' '*n2,diff)
        i=i+1
        
test_square_root()

#练习7-2
#有个是我想多了，如果要接受import岂不是直接要写个解释器？
def eval_loop():
    while(True):
       enter=input('>')
       if(enter=='done'):
        print(anser)
        break
       else:
        anser=eval(enter)
       print(anser)
   
#eval_loop()  