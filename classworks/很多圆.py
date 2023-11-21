import turtle
t = turtle.Pen()
t.speed(10)
t.width(2)

first_color = "red"
second_color = "green"
thrid_color = "orange"
fourth_color = "blue"
fifth_color = "yellow"
term=0
x=0
y=0
radius = 10

for i in range (5):
    t.color(fifth_color)
    t.circle(radius)
    t.penup()
    term = term+1
    x=term*20
    t.setpos(x,y)
    t.pd()

term = 0
t.penup()
y=20
x=0
t.setpos(x,y)
t.pd()

for i in range (4):
    t.color(fourth_color)
    t.circle(radius)
    t.penup()
    term = term+1
    x=term*20
    t.setpos(x,y)
    t.pd()

term = 0
t.penup()
y=40
x=0
t.setpos(x,y)
t.pd()

for i in range (3):
    t.color(thrid_color)
    t.circle(radius)
    t.penup()
    term = term+1
    x=term*20
    t.setpos(x,y)
    t.pd()

term = 0
t.penup()
y=60
x=0
t.setpos(x,y)
t.pd()

for i in range (2):
    t.color(second_color)
    t.circle(radius)
    t.penup()
    term = term+1
    x=term*20
    t.setpos(x,y)
    t.pd()

term = 0
t.penup()
y=80
x=0
t.setpos(x,y)
t.pd()

t.color(first_color)
t.circle(radius)
t.penup()
term = term+1
x=term*20
t.setpos(x,y)
t.pd()
