import turtle

t=turtle.Pen()
dot_diameter = 3
#print(t.width())
t.lt(180)

for i in range (10):
    t.dot(dot_diameter)
    t.write(-(i),align = "center")
    t.fd(dot_diameter/2+10)
