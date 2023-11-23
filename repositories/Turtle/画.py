import turtle

colors = ["red","purple","blue","green","orange","yellow"] #创建color列表
t=turtle.Pen()
turtle.bgcolor("black")#调整背景颜色

for x in range(360):
    t.pencolor(colors[x%6])#根据循环次数定画笔颜色
    t.pencolor()
    t.width(x/100+1)#根据循环次数定笔的粗细
    t.fd(x)#走循环次数个单位的长度
    t.lt(59)