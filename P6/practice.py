import math

def campare(a,b):
    if(a>b):
        return 1
    elif(a<b):
        return -1
    else:
        return 0
        

def hypotenuse(a,b):
    c = math.sqrt(a**2+b**2)
    return c
    

def is_between(x,y,z):
    return (x<=y and y<=z)


def factorial(n):
    space =' '*(4*n)
    print( space, 'factorial', n)
    if n == 0:
        print( space, 'returning 1')
        return 1
    else:
        recurse = factorial( n- 1)
        result = n * recurse
        print( space, 'returning', result)
        return result

#练习6-1
def b(z):
    prod =a(z,z)
    print(z,prod)
    return prod
   
def a(x,y):
    x=x+1
    return x*y

def c(x,y,z):
    total =x+y+z
    square=b(total)**2
    return square
    
#练习6-2
#当n>4或者m>8时，报错是
#maximum recursion depth exceeed in comparision
def ack(m,n):
    if m==0:
        return n+1
    elif(m>0 and n==0):
        return ack(m-1,1)
    elif(m>0 and n>0):
        return ack(m-1,ack(m,n-1))
    else:
        print('WRONG!')
        return

#练习6-5
#完美啊
def gcd(a,b):
    if (type(a)==type(b)== int):
        if(a<b):
            c=a
            a=b
            b=c
        elif(a>b):
           r=a%b
           if(r==0):
            return b
           elif((b%r)==0):
            return r
           else:
            r=gcd(b,r)
            return r
        elif(a==b):
            return b
    else:
        return('Please enter integer')
        
print(gcd(800,56))