'''
16-th homework 3rd question
在15.3.py的基础上，使得气球上升的时候彼此之间不碰撞。
优先级：中
预估完成时长:30 - 60 min
实际：
'''
from tkinter import *
import random,time

win=Tk()
c=Canvas(win,width=1000,height=1000)

height_of_ballon=90
width_of_ballon=50
number_of_balloons=1

balloons_coords=[]

c.pack()
overlap=True
overlap_ture_or_false=[]
final_result=1

#创建一个判断是否重叠的程序
def determine_overlap(compared_balloon_index,list_of_balloon_coords):
    global overlap
    for index,coords in enumerate(list_of_balloon_coords):
        #排除所有重叠可能性(左上角重叠，右上角重叠，左下角重叠，右上角重叠)
        if list_of_balloon_coords[compared_balloon_index][0]<=coords[0]+width_of_ballon and\
        list_of_balloon_coords[compared_balloon_index][0]+width_of_ballon>=coords[0] and\
        list_of_balloon_coords[compared_balloon_index][1]+height_of_ballon>=coords[1] and \
        list_of_balloon_coords[compared_balloon_index][1]<=coords[1]+height_of_ballon:
            if compared_balloon_index==index:
                overlap=False
            else:
                overlap=True
        else:
            overlap=False
        overlap_ture_or_false.append(overlap)

for latitude in range (600):#飞多高
    for index_of_balloons in range(number_of_balloons):#生成几个气球
        if latitude==0:
            x_coord=random.randint(10,int(c.cget("width"))-width_of_ballon)#生成坐标
            y_coord=random.randint(int(c.cget("height"))-500,int(c.cget("height"))-height_of_ballon)#生成坐标
            balloons_coords.append([x_coord,y_coord])
        oval=c.create_oval(balloons_coords[index_of_balloons][0],balloons_coords[index_of_balloons][1],\
                        balloons_coords[index_of_balloons][0]+width_of_ballon,balloons_coords[index_of_balloons][1]+height_of_ballon,\
                        fill="red")#生成气球
        for index in range(len(overlap_ture_or_false)):
            if index+1==len(overlap_ture_or_false):
                break
            final_result=overlap_ture_or_false[index]+overlap_ture_or_false[index+1]
        while final_result>0:
            determine_overlap(index_of_balloons,balloons_coords)
            balloons_coords.clear()
            for index_of_balloons in range(number_of_balloons):
                x_coord=random.randint(10,int(c.cget("width"))-width_of_ballon)#生成坐标
                y_coord=random.randint(int(c.cget("height"))-500,int(c.cget("height"))-height_of_ballon)#生成坐标
                balloons_coords.append([x_coord,y_coord])
    for balloons in balloons_coords:
    #移动气球
        if latitude%2>0:
            balloons[0]-=10
        else:
            balloons[0]+=10
        balloons[1]-=latitude*1
    c.update()
    time.sleep(1)
    c.delete("all")

c.mainloop()