'''
12-th homework 4th question
画出如该相对路径所示动画："homework/image/12.4.GIF"
'''

from tkinter import *
import time

win=Tk()
c=Canvas(win,width=1000,height=800)

b_rec=c.create_rectangle(0,350,100,450,fill="blue")
r_rec=0 #提前定义r_rec

#制作场地
c.create_line(650,0,650,800)

#移动长方形
for i in range (900):
    #判断是否需要改颜色
    if i==549:
        r_rec=c.create_rectangle(550,350,650,450,fill="red")
        c.delete(b_rec)
    else:
        c.move(b_rec,1,0)
        c.pack()
        c.update()
        time.sleep(0.01)
    c.move(r_rec,1,0)
    c.pack()
    c.update()
    time.sleep(0.01)
    c.create_line(650,0,650,800)


