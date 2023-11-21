import turtle

#draw river (circle)
##define river and give attribute
river=turtle.Pen()
river.speed(30)
river.width(100)
river.color("blue")
river.circle(250)

#make turtle (t) and turtle 2(x) swim 
##define t and x and give attribute
t=turtle.Pen()
x=turtle.Pen()
t.shape("turtle")
t.color("black")
x.shape("turtle")
x.color("white")
t.speed(10)
t.penup()
x.penup()
t.ht()
t.setpos(0,25)
t.st()
for i in range (360):
    t.fd(20)
    t.lt(5)
    x.fd(20)
    x.lt(5)
