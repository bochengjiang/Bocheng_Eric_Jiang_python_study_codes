import turtle
t=turtle.Pen()
t.shape("turtle")
t.color("blue")
t.width(5)

small_circle_radius = 100
big_circle_radius = 200

t.circle(big_circle_radius)
t.penup()
t.setpos(0,small_circle_radius)
t.pendown()
t.circle(small_circle_radius)
