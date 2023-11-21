import turtle
t = turtle.Pen()
t.speed(10)

t.shape ("turtle")
t.color('blue')
pen_color=["red","yellow"]
pen_color_1="red"
pen_color_2="yellow"
small_distance = 60
big_distance = 300-small_distance*2
angle = 180-30

for i  in range(12):
    t.color(pen_color_1)
    t.forward(small_distance)
    t.color(pen_color_2)
    t.fd(big_distance)
    t.color(pen_color_1)
    t.fd(small_distance)
    t.left(angle)
