
def check_fermat(a,b,c,n):
    if((a**n+b**n==c**n)and(n>2)):
        print('oh no,Fermat is wrong!')
    else:
        print('don`t do that')
        
a=int(input("please enter 'a'\n"))
b=int(input("please enter 'b'\n"))
c=int(input("please enter 'c'\n"))
n=int(input("please enter 'n'\n"))

check_fermat(a,b,c,n)       
    