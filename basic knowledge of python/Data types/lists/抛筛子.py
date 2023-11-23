import random,turtle,time

#define t and give attribute
t=turtle.Pen()
t.ht()
t.speed(0)
t.pu()
result=[]

for i in range (10):
    #create dice_number for how big the result is
    dice_number = random.randint(1,6)
    result.append(dice_number)
    #draw dot
    for i in range(dice_number):
        t.dot()
        t.pu()
        t.fd(50)
    time.sleep(1)
    t.clear()
    t.setpos(0,0)
    #print(dice_number)
print(result)