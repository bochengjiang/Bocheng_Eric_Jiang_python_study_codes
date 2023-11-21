import turtle
import time
t=turtle.Pen()
t.width(1)
t.ht()
t.speed(30)


t.lt(90)
for i in range(60):
    t.forward(100)
    t.penup()
    t.setpos(0,0)
    t.pd()
    t.right(6)
    time.sleep(1)
    t.clear()
    
