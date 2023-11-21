import random,turtle,time

for i in range (10):
    a=random.randint(10,100)-10
    print (a)

t=turtle.Pen()
b = t.fd(10)
c=time.sleep(random.randint(1,10))
print(type(b),b,type(c),c)
