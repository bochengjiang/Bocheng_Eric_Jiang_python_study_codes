import turtle
#define x
x=turtle.Pen()
x.turtlesize(3)
x.shape("turtle")
x.color("grey")
#define y
y=turtle.Pen()
y.shape("turtle")
y.color("orange")

for i in range (10):
    y.fd(100)
    y.lt(90)
    x.fd(100)
    x.lt(90)
y.bk(100)
x.speed(8)
for i in range (50):
    x.fd(100)
    x.lt(90)
