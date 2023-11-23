'''
14-th homework 1st question
如该相对路径所示动画："homework/image/14.1.gif"
完成程序的编写，使得可以用键盘四个方向键操控吃豆人吃屏幕上的豆子

预估完成时长:60 - 120 min
实际：
'''

from tkinter import *
import random

win=Tk()
c=Canvas(win,width=1000,height=1000)

def eat_food_module():
    for index,each_dot in enumerate(dot_coords):
        if each_dot[0]>squ_coord[0] and each_dot[1]>squ_coord[1]\
            and each_dot[2]<squ_coord[2] and each_dot[3]<squ_coord[3]:
            delete_item=dot_name[index]
            c.delete(delete_item)
            c.update()

def move_obj(event):
    global squ_coord
    if event.keysym == "Up":
        if squ_coord[1]>=0:
            c.move(obj,0,-10)
    elif event.keysym == "Down":
        if squ_coord[3]<=int(c.cget("height")):
            c.move(obj,0,10)
    elif event.keysym == "Left":
        if squ_coord[0]>=0:
            c.move(obj,-10,0)
    elif event.keysym=="Right":
        if squ_coord[2]<=int(c.cget("width")):
            c.move(obj,10,0)
    c.update()
    squ_coord=c.coords(obj)
    eat_food_module()

obj=c.create_rectangle(10,100,110,200,fill="blue")
c.pack()
c.update()

squ_coord=c.coords(obj)

dot_name=[]
dot_coords=[]

#创造食物
for number_of_dots in range(6):
    x_coord=random.randint(1,int(c.cget("width")))
    y_coord=random.randint(1,int(c.cget("height")))
    food=c.create_oval(x_coord,y_coord,x_coord-10,y_coord-10,fill="Yellow")
    food_coord=c.coords(food)
    dot_coords.append(food_coord)
    dot_name.append(food)
c.update()

#绑定键盘案件
c.bind_all("<KeyPress>",move_obj)

len_dot_coords=len(dot_coords)

c.mainloop()