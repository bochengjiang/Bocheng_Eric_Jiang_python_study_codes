import turtle
t = turtle.Pen()
t.shape("turtle")
angle=144
distance=150
t.speed(0)
i=0
while True:
    if i%5 == 0:
        t.color("blue")
    if i%5 == 1:
        t.color("red")
    if i%5 == 2:
        t.color("orange")
    if i%5 == 3:
        t.color("pink")
    if i%5 == 4:
        t.color("purple")
        #t.rt(18)
        #t.fd(10)
        #t.lt(18)
    i=i+1
    distance=distance+1
    t.forward(distance)
    t.left(angle)




