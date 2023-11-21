'''
16-th homework 2nd question
在15.2.py代码的基础上修改，使得小人可以更随机地奔跑（连续移动的基础上更随机），如图image/15.2.GIF所示
优先级：中
预估完成时长:30 - 60 min
实际：
'''
from tkinter import *
import time, random

win=Tk()
c=Canvas(win,height=1000,width=1000)
c.pack()

#1. 导入所有图片
running_man_pics={}

for pic_num in range(6):
    running_man_pics[pic_num+1]=PhotoImage(file=f"homework\image\people\man{(pic_num+1)}.gif")

single_man_running=[]
#2. 让每个小人跑起来成为动图
running_man=[]

x_y_random_coords=[]
x_range_number=3
y_range_number=3

for i in range (200):#一直跑
    for y in range (y_range_number):
    #列数
        x_y_random_coords.append([])
        for x in range (x_range_number):
        # 行数
            x_pos_or_neg=random.randint(-1,1)
            y_pos_or_neg=random.randint(-1,1)
            x_y_random_coords[y].append([x_pos_or_neg,y_pos_or_neg])
            x_coord_per_man=((running_man_pics[1].width()-150)*x+150)
            y_coord_per_man=((running_man_pics[1].height()-105)*y+150)
            new_x=x_coord_per_man+x_y_random_coords[y][x][0]*(i*10)
            new_y=y_coord_per_man+x_y_random_coords[y][x][1]*(i*10)
            running_man_frame=c.create_image(new_x,new_y,anchor="nw", image=running_man_pics[i%6+1])
            move_x=random.randint(-50,50)
            move_y=random.randint(-50,50)
            c.move(running_man_frame,move_x,move_y)
    c.update()
    time.sleep(0.1)
    c.delete("all")
