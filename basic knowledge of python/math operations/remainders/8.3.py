# 8-th homework 3rd question
## 画一排正方形与三角形交替出现的图案
## 代码尽可能优雅，简练

import turtle

t=turtle.Pen()

for i in range (10):
    if i%3==0:
        for a in range(4):
            t.fd(10)
            t.lt(90)        
    elif i%3==1:
        for b in range(3):
            t.fd(10)
            t.lt(120)
    elif i%3==2:
        for b in range(5):
            t.fd(10)
            t.lt(72)
    t.fd(10)
