import turtle, random

#defining food
food_1=turtle.Pen()

#giving attribute to food_1
food_1.pu()
food_1.ht()

#cloning other foods
food_2=food_1.clone()
food_3=food_1.clone()

#distrubuting foods
for i in range(3):
    x=random.randint(-(250),250)
    y=random.randint(-(250),250)
    if i==0:
        food_1.setpos(x,y)
    elif i==1:
        food_2.setpos(x,y)
    else:
        food_3.setpos(x,y)

#returning current position
food_1_pos=food_1.pos()
food_2_pos=food_2.pos()
food_3_pos=food_3.pos()

#creating turtle
t=turtle.Pen()
t.shape("turtle")
t.pu()

#set value for foods
value_of_food_1 = random.randint(20,80)
value_of_food_2 = random.randint(20,80)
value_of_food_3 = random.randint(20,80)

food_1.write(str(value_of_food_1),align="center",font=(20))
food_2.write(str(value_of_food_2),align="center",font=(20))
food_3.write(str(value_of_food_3),align="center",font=(20))

#create amount eat by turtle
turtle_amount = 0

#turtle eat and move
for i in range (50):
    t.fd(random.randint(-(100),100))
    t.lt(random.randint(0,180))
    t_pos=t.pos()
    # turtle eat jugdment
    if t_pos == food_1_pos:
         food_1.clear()
         food_1.color("red")
         food_1.write(value_of_food_1,align="center",font=(20))
         turtle_amount=turtle_amount+value_of_food_1
    elif t_pos == food_2_pos:
         food_2.clear()
         food_2.color("red")
         food_2.write(value_of_food_2,align="center",font=(20))
         turtle_amount=turtle_amount+value_of_food_2
    elif t_pos == food_3_pos:
         food_3.clear()
         food_3.color("red")
         food_3.write(value_of_food_3,align="center",font=(20))
         turtle_amount=turtle_amount+value_of_food_3
    
         




    
