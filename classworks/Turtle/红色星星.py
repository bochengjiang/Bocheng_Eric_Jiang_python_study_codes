import turtle
t = turtle.Pen()
t.shape("turtle")
angle=144
distance=150
t.color("yellow")
turtle.colormode(255)
t.fillcolor(255,0,0)
t.begin_fill()
for i in range (4):
    t.forward(distance)
    t.left(angle)
t.forward(distance)
t.end_fill()
