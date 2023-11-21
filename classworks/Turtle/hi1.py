import turtle
t = turtle.Pen()

t.shape("turtle")
t.color("red",'blue')
left_angle = 130
right_angle = left_angle-75

for i in range (5):
    t.forward(100)
    t.left(left_angle)
    t.forward(100)
    t.right(right_angle)



