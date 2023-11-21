import turtle
t=turtle.Pen()
t.color("green")
distance = 25
angle = 90

for i in range (4):
    t.fd(distance)
    t.lt(angle)
    for i in range(2):
        t.fd(distance)
        t.rt(angle)
    #t.fd(distance)
    #t.rt(angle)
    t.fd(distance)
    t.lt(angle)
