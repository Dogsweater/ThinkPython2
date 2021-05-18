import turtle

def koch(t,length):
    if (length<3):
        t.fd(length)
        return
    koch(t,length/3)
    t.lt(60)
    koch(t,length/3)
    t.rt(120)
    koch(t,length/3)
    t.lt(60)
    koch(t,length/3)

def snowflake(t,length):
    koch(t,length)
    t.rt(120)
    koch(t,length)
    t.rt(120)
    koch(t,length)

bob=turtle.Turtle()
snowflake(bob,90.0)
turtle.mainloop()