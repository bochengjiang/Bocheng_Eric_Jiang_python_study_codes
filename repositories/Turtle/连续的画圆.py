import turtle
t=turtle.Pen()
t.color("red")
t.width(3)

radius = 30
x=0
term=0

for i in range (5):
    t.circle(radius)
    t.penup()
    #term = term+1
    x=(i+1)*radius*2
    t.setpos(x,0)
    t.pd()
    print(i)


