import copy

class Point:
    """Represents a point in 2-D space"""
    
class Rectangle:
    """Attributes:width,height,corner"""
        
box=Rectangle()
box.width=100.0
box.height=200.0
box.corner=Point()
box.corner.x=0.0
box.corner.y=0.0

def print_point(p):
    print('(%g,%g)'%(p.x,p.y))

#实例作为参数传入时，会发生改变
def find_center(rect):
    p=Point()
    p.x=rect.corner.x+rect.width/2
    p.y=rect.corner.y+rect.height/2
    return p
    
center=find_center(box)
#print_point(center)
p1=Point()
p1.x=3.0
p1.y=4.0

p2=copy.copy(p1)
#print_point(p2)

#浅复制
box2=copy.copy(box)
print(box2 is box)
print(box2.corner is box.corner)

#深复制
box3=copy.deepcopy(box)
print(box3 is box)
print(box3.corner is box.corner)

def move_rectangle(rect,p):
    rect_=copy.deepcopy(rect)
    rect_.corner.x+=p.x
    rect_.corner.y+=p.y
    return rect_
   
new_box=move_rectangle(box,p2)
print_point(new_box.corner)
    