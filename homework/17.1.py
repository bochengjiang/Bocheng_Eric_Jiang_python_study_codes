'''
17-th homework 1st question
实现如该相对路径所示动画："homework/image/17.1.gif"

预估完成时长:60 - 120 min
实际：
'''
from tkinter import *
import random,time,copy

win=Tk()
c=Canvas(win,width=1000,height=1000)

c.pack()

#def detect_in_squr():
#判断游戏是否要结束
# user_input=input("是否开始游戏:")

#生成随机坐标
moving_rec_size=50
upper_x_coor=random.randint(10,int(c.cget("width"))-10-moving_rec_size)
upper_y_coor=random.randint(10,int(c.cget("height"))-10-moving_rec_size)
blue_rec_x_coord=int(c.cget("width"))*1/3
blue_rec_y_coords=int(c.cget("height"))*1/3

#创建移动的长方形
moving_rec=c.create_rectangle(upper_x_coor,upper_y_coor,upper_x_coor+moving_rec_size,upper_y_coor+moving_rec_size,fill="red")
blue_rec=c.create_rectangle(blue_rec_x_coord,blue_rec_y_coords,\
                            blue_rec_x_coord*2,blue_rec_y_coords*2,fill="blue")

#随机生成移动方向
move_x=random.choice([-3,3])
move_y=random.choice([-3,3])

def determine_overlap_and_delete_squr(moving_squr_coords,blue_squr_coords):
    global blue_rec
    if moving_squr_coords[2]>=blue_squr_coord[0] and moving_squr_coords[0]<=blue_squr_coords[2]\
    and moving_squr_coords[3]>=blue_squr_coords[1] and blue_squr_coords[3]>=moving_squr_coords[1]:
        c.itemconfig(blue_rec,state='hidden')
        c.itemconfig(moving_rec,fill='purple')
    else: 
        c.itemconfig(blue_rec,state='normal')
        c.itemconfig(moving_rec,fill='red')

#获取两个方形的坐标
squr_coord=c.coords(moving_rec)
blue_squr_coord=c.coords(blue_rec)

while True:
    c.move(moving_rec,move_x, move_y)
    squr_coord=c.coords(moving_rec)
    determine_overlap_and_delete_squr(squr_coord,blue_squr_coord)
    if squr_coord[0]<=0 or squr_coord[2]>=int(c.cget("width")):#确认小方块左上角等于左边边框或者右下角等于画布右边边框
        move_x=-move_x
    if squr_coord[1]<=0 or squr_coord[3]>=int(c.cget("height")):
        move_y=-move_y
    time.sleep(0.01)
    c.update()