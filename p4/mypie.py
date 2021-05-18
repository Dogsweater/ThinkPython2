'''
懒得看参考了，我这个真有趣，233
'''
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
    
#debug:cos默认是弧度   
def pie(t,n,length):
    angle1=360/n
    angle2=(180-angle1)/2
    b=(length/2)/(math.cos(math.radians(angle2)))
    t.lt(180-angle2)
    t.fd(b)
    for i in range(n):    
        t.lt(180-angle1)
        t.fd(b)
        t.lt(180)
        t.fd(b)
    t.lt(180-angle1)
    t.fd(b)
    t.lt(180-angle2)
    polygon(bob,n,length)
#虽然它很奇怪但是它是对的

def move(t,length):
        t.pu()
        t.fd(length)
        t.pd()
        
bob=turtle.Turtle()
move(bob,-200)
pie(bob,5,60)
move(bob,200)
pie(bob,6,60)
move(bob,200)
pie(bob,7,60)
move(bob,200)
pie(bob,8,60)
turtle.mainloop()
