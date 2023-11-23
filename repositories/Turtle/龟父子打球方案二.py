import turtle

# define and give attribute to son
son = turtle.Pen()
son.shape("turtle")
son.color("blue")
son.speed(0)
son.pu()
son.setpos(-(100),0)
son.speed(3)

# define and give attribute to dad
dad = turtle.Pen()
dad.shape("turtle")
dad.color("blue")
dad.speed(0)
dad.turtlesize(2,2)
dad.pu()
dad.setpos(100,0)
dad.lt(180)
dad.speed(3)

# define and give attribute to t
t = turtle.Pen()
t.pu()
t.setpos(-(80),0)
t.shape("circle")

#make dad and son kick the ball (t)
for i in range(100):
    son.fd(10)
    son.bk(10)
    t.fd(160)
    dad.fd(10)
    dad.bk(10)
    t.bk(160)
    #dad.bk(5)
