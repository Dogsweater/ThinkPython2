'''
对比给出的示例：
示例是分为花瓣和花函数
它找到了每次转的角度是360/n （n是花瓣数）
其他的差不多
'''
import turtle
import math

def polyline(t,n,length,angle):
    t.delay=0.001
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def acr(t,r,angle):
    acrlength=math.pi*r*2*angle/360
    n=int(acrlength/3)+1
    step_length=acrlength/n
    step_angle=float(angle/n)
    polyline(t,n,step_length,step_angle)

#要求：angle<180,turn_angle<180
'''
一个问题记录：在没有第35行bob.lt(flower_angle)时，我的花还是不能炮姐
能成的是弧-转-弧-转，我的是弧-转-弧 少一个转
为什么不行？ 将角度修正到o方向？
'''
def flower(t,r,n,angle):
    flower_angle=180-angle
    turn_angle=360.0/n
    for i in range(n):
        acr(t,r,angle)
        bob.lt(flower_angle)
        acr(t,r,angle)
        bob.lt(flower_angle)
        bob.lt(turn_angle)

def move(t,length):
        t.pu()
        t.fd(length)
        t.pd()
       
bob =turtle.Turtle()
bob.delay=0.01
move(bob,-100)
flower(bob,60.0,7,60.0)
move(bob,120)
flower(bob,40.0,10,80.0)
move(bob,120)
flower(bob,140.0,20,20.0)
'''
#循环次数：花瓣的朵数
#r半径，angle越小花瓣越窄
#lt度数越大花瓣越密集
#缺点：花瓣数应该和angel和lt有关，以便画出完整的花朵，但是没有找到关系
for i in range(20):
    acr(bob,100,30)
    bob.lt(150)
    acr(bob,100,30)
    bob.lt(20)
'''
turtle.mainloop()