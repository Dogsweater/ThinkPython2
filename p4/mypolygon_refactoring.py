import turtle
import math

def polyline(t,n,length,angle):
    t.delay=0.001
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    
def polygon(t,n,length):
    angle = 360/n
    polyline(t,n,length,angle)

"""  可以用acr函数  
def circle(t,r):
    circumference = math.pi*r*2
    n= int(circumference/3)+1
    length=circumference/n
    angle=360/n
    polyline(t,n,length,angle)
"""

'''
#命名不是很好,用acrlenth代替circumference，step_length代替length,step_angle代替t_angle 
#和书上的思路不一样，我是用time控制弧度，而书是直接用周长控制的 ，更方便
def acr(t,r,angle):
    circumference_circle=math.pi*r*2
    circumference = circumference_circle*angle/360
    n=int(circumference_circle/3)+1
    times= int(n*angle/360)+1
    length= circumference_circle/n
    t_angle = 360/n
    polyline(t,times,length,t_angle)
'''

#第一次  step_angle=angle/n没有转换为float，不好
#注意检查形参def acr(t,r,angle):
def acr(t,r,angle):
    acrlength=math.pi*r*2*angle/360
    n=int(acrlength/3)+1
    step_length=acrlength/n
    step_angle=float(angle/n)
    polyline(t,n,step_length,step_angle)

def circle(t,r):
    acr(t,r,360)

bob =turtle.Turtle()
polygon(bob,5,100)
turtle.mainloop()