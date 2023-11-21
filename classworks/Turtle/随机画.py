import turtle, random

t = turtle.Pen()

for i in range (100):
    distance = random.randint(10,100)
    #print (distance)
    angle = random.randint(0,360)
    #print (angle)
    t.fd(distance)
    t.lt(90)
