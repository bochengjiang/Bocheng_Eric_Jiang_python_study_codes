import turtle
t = turtle.Pen()
t.shape("turtle")
angle=144
distance=10
t.speed(0)
i=0
turtle.bgcolor("black")
color_list=["blue","red","orange","pink","purple"]
while i<500:
    t.color(color_list[i%5])
    i=i+1
    distance=distance+2
    t.forward(distance)
    t.left(angle)
