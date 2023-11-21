import turtle

t = turtle.Pen()
distance = 10

for i in range (20):
    if distance%80==20:
        t.color("gold")
    if distance%40==30:
        t.color("green")
    if distance%40==0:
        t.color("red")
    if distance%40==10:
        t.color("blue")
    t.fd(distance)
    distance=distance+10
    t.lt(90)
    t.color("black")
    print(distance)



