import turtle, random

t = turtle.Pen()
t.shape("turtle")

t.lt(90)

for i in range (10):
    random_number=random.randint(1,10)
    if random_number>6:
        t.fd(80)
    print (random_number)
