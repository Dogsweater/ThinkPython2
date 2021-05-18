import math

class Circle():
    """P:center,radius"""
    
class Point:
    """Represents a point in 2-D space"""
 
center1=Point()
center1.x=150
center1.y=100
cir1=Circle()
cir1.center=center1
cir1.r=75

p1=Point()
p1.x=150
p1.y=60

def point_in_circle(p,cir):
    d=math.sqrt((cir.center.x-p.x)**2+(cir.center.y-p.y)**2)
    if(d<=cir.r):
        return True
    else:
        return False

print(point_in_circle(p1,cir1))