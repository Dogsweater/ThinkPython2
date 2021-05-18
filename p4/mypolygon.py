#P4 书中练习
#其实做的时候是一步一步做的，有点TDD的感觉
import turtle
import math

def square(t,length):
    print(t)
    t.pd()
    for i in range(4):
        t.lt(90)
        t.fd(length)

#turtle要转的角度事实上就是多边形的内角度数，而多边形的内角和是360°
def polygon(t,length,n):
    print(t)
    t.pd()
    for i in range(n):
        t.lt(360/n)
        t.fd(length)

#原来计算机画圆是这样画的吗，厉害了
#相当于割圆术，n越大则精度越大
#计算每次画的长度时，用周长算
#看书之后发现可以复用polygon函数
#看书之后发现n与精度和效率都有关系，智能的计算n更好
#修改代码为 n=int(circumference/3)+1
def circle(t,r):
    t.delay=0.001
    circumference=math.pi*r*2
    n=100
    length=circumference/100
    polygon(t,length,n)

#第一次做的时候出现的问题是不知道怎么控制弧度
#第二个出现的问题是直接t.fd(circumference/100)，没有还原circumference
def acr(t,r,angle):
    print(t)
    t.delay=0.001
    t.pd()
    circumference=(math.pi*r*2)*angle/360
    print(circumference)
    n=int(100*angle/360)
    for i in range(n):
        t.lt(360/100)
        t.fd(circumference*360/angle/100)

bob=turtle.Turtle()
circle(bob,200)
turtle.mainloop()


