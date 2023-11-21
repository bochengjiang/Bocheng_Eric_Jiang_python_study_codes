import turtle, random

t=turtle.Pen()
t.pd()
t.shape("turtle")

total_value=0

for i in range (5):
    t.pu()
    x=random.randint(-(250),250)
    y=random.randint(-(250),250)
    t.setpos(x,y)
    gold_weight = random.randint(0,10)
    gold_ratio = random.random()
    if gold_weight<=6 and gold_ratio<0.5:
        t.fillcolor("gold")
        t.pd()
        t.begin_fill()
        t.circle(gold_weight)
        t.end_fill()
        t.write(str(gold_weight*gold_ratio/10))
        t.pu()
        total_value=total_value+gold_weight*gold_ratio/10
        #print(gold_ratio,gold_weight,total_value)
    else:
        t.fillcolor("grey")
        t.pu()
        t.begin_fill()
        t.circle(gold_weight)
        t.end_fill()
        t.write(str(gold_weight*gold_ratio/10))
        t.pu()
        print(gold_ratio,gold_weight)

t.home()
t.pu()
t.write("{:.2f}".format(total_value),font=(250))
