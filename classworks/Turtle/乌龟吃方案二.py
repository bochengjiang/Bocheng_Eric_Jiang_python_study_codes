import turtle, random

t=turtle.Pen()
t.shape("turtle")
t.speed(0)

turtle_weight = 0
dont_eat=0

for i in range (50):
    t.pu()
    x=random.randint(-(250),250)
    y=random.randint(-(250),250)
    t.setpos(x,y)
    food_weight = random.randint(20,80)
    if food_weight > 60:
        t.color("red")
        t.pd()
        t.write(str(food_weight),font=(50))
        turtle_weight=turtle_weight+food_weight
    else:
        t.color("grey")
        t.pd()
        t.write(str(food_weight),font=(50))
        dont_eat=dont_eat+1
        if dont_eat == 10:
            t.pu()
            t.home()
            t.write("I am tired~~",font=(250))
            break
            
    if turtle_weight > 250:
        #print(t.isdown())
        t.pu()
        t.home()
        t.write("I am full ~~~",font=(250))
        break



