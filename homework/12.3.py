'''
12-th homework 3rd question
画出如该相对路径所示动画："homework/image/12.3.gif"
图片素材：
> homework/people

预估完成时长：90 - 120 min

'''

from tkinter import *
import time, random

win=Tk()
c=Canvas(win,height=1000,width=1000)
c.pack()
running_man_group_1=[]
running_man_group_2=[]
running_man_group_3=[]
running_man_group_4=[]

#1. 导入所有图片
running_man_pics={}

for pic_num in range(6):
    running_man_pics[pic_num+1]=PhotoImage(file=f"homework\image\people\man{(pic_num+1)}.gif")

single_man_running=[]
#2. 让每个小人跑起来成为动图
running_man=[]

pos_or_neg=random.choice([1,-1])

for i in range (160):#一直跑
    for y in range (6):
    #列数
        for x in range (6):
        # 行数
            x_coord_per_man=((running_man_pics[1].width()-150)*x+150)
            y_coord_per_man=((running_man_pics[1].height()-105)*y+150)
            if x<3:
                new_x=x_coord_per_man+i*10
            else:
                new_x=x_coord_per_man-i*10
            if y<3:
                new_y=y_coord_per_man+i*10
            else:
                new_y=y_coord_per_man-i*10
            running_man_frame=c.create_image(new_x,new_y,anchor="nw", image=running_man_pics[i%6+1])
    c.update()
    time.sleep(0.09)
    c.delete("all")#无法删除之前的人

print (running_man_group_1)

'''
1. 导入所有图片
2. 让每个小人跑起来成为动图
3. 使人排成4个3*3的正方形
4. 以每一个正方形为单位,让这四个分别向nw,ne,se,sw的方向跑
'''