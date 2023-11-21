'''
13-th homework 1st question
画出如该相对路径所示动画："homework/image/13.1.gif"
注意，小球移动的方向是随机的

预估完成时长：60 - 120 min

'''
from tkinter import *
import time, random

win=Tk()
c=Canvas(win,width=1000,height=1000)

#为小球随机定一个出现的位置
ball_size=50
upper_x_coor=random.randint(10,int(c.cget("width"))-10-ball_size)
upper_y_coor=random.randint(10,int(c.cget("height"))-10-ball_size)

circle=c.create_oval(upper_x_coor,upper_y_coor,upper_x_coor+ball_size,upper_y_coor+ball_size,fill="red")

move_x=0
move_y=0

while move_x==0 and move_y==0:
    move_x=random.randint(-10,10)
    move_y=random.randint(-10,10)

cir_coord=c.coords(circle)
for i in range (10):
    while cir_coord[0]>=0 and cir_coord[1]>=0\
        and cir_coord[2]<=int(c.cget("width")) and cir_coord[3]<=int(c.cget("height")):
        c.move(circle,move_x,move_y)
        c.pack()
        c.update()
        cir_coord=c.coords(circle)
        time.sleep(0.01)
    move_x=random.randint(-10,10)
    move_y=random.randint(-10,10)
    while move_x==0 and move_y==0 or (cir_coord[0]+move_x)<=0 or \
        (cir_coord[1]+move_y)<=0\
        or (cir_coord[2]+move_x)>=int(c.cget("width")) or \
            (cir_coord[3]+move_y)>=int(c.cget("height")):
        move_x=random.randint(-10,10)
        move_y=random.randint(-10,10)
    c.move(circle,move_x,move_y)
    cir_coord=c.coords(circle)


'''
1. 小球随机出现
2. 小球朝随机方向走
3. 小球碰壁后反弹
'''