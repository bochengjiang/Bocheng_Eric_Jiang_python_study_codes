'''
15-th homework 3rd question
完成如图15.3.GIF所示的气球放飞的动图。
代码在完成实现需求的基础上，可以尽可能地优化
预估完成时长:30 - 60 min，优化预估时长：30 - 60 min
实际：大概147分钟
'''
from tkinter import *
import random,time

win=Tk()
c=Canvas(win,width=1000,height=1000)

balloons=[]
height_of_ballon=90
width_of_ballon=50

balloons_coords=[]

c.pack()

for latitude in range (600):#飞多高
    for index_of_ballons in range(6):#生成几个气球
        if latitude==0:
            x_coord=random.randint(10,int(c.cget("width"))-width_of_ballon)
            y_coord=random.randint(int(c.cget("height"))-500,int(c.cget("height"))-height_of_ballon)
            balloons_coords.append([x_coord,y_coord])
        oval=c.create_oval(balloons_coords[index_of_ballons][0],balloons_coords[index_of_ballons][1],\
                        balloons_coords[index_of_ballons][0]+width_of_ballon,balloons_coords[index_of_ballons][1]+height_of_ballon,\
                        fill="red")
    for balloons in balloons_coords:
        if latitude%2>0:
            balloons[0]-=10
        else:
            balloons[0]+=10
        balloons[1]-=latitude*1
    c.update()
    time.sleep(0.1)
    c.delete("all")

c.mainloop()
