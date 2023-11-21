import turtle

# define and give attribute to son
son = turtle.Pen()
son.shape("turtle")
son.color("blue")
son.speed(0)
son.pu()
son.setpos(-(100),0)
son.speed(1)

# define and give attribute to dad
dad = turtle.Pen()
dad.shape("turtle")
dad.color("blue")
dad.speed(0)
dad.turtlesize(2,2)
dad.pu()
dad.setpos(100,0)
dad.lt(180)
dad.speed(1)

# define and give attribute to t
t = turtle.Pen()
t.ht()
t.pu()
t.setpos(-(80),0)
t.speed(0)

#define and give attribute to x
x = turtle.Pen()
x.ht()
x.pu()
x.setpos(-(80),0)
x.speed(0)

#make dad and son kick the ball (t)
for i in range(100):
    son.fd(10)
    son.bk(10)
    for i in range (16):
        t.fd(10)
        t.dot()
        x.clear()
        x.fd(10)
        x.dot()
        t.clear()
    dad.fd(10)
    dad.bk(10)
    for i in range (16):
        t.bk(10)
        t.dot()
        x.clear()
        x.bk(10)
        x.dot()
        t.clear()








    
