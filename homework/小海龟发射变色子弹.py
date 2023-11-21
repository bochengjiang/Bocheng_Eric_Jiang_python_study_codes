import turtle, random

t=turtle.Pen()
bullet=turtle.Pen()

t.shape("turtle")
turtle.resizemode("user")
t.turtlesize(2.0,2.0,1)

bullet_color=["red","Yellow","blue"]
bullet_shape=["circle","turtle","triangle"]
bullet.pu()
bullet.turtlesize(0.5,0.5,0.1)

for i in range(500):
    bullet.fd(5)
    bullet.color(bullet_color[i%3])
    bullet.shape(bullet_shape[i%3])

