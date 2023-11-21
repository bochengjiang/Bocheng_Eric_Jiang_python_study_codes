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

height_of_ballon=100
width_of_ballon=100
number_of_balloons=6
true_or_false=False
yes_no_break=False

balloons_coords=[]

c.pack()

#创建一个判断是否重叠的程序
def generate_x_y():
    list_of_balloons=[]
    for i in range (number_of_balloons):
        x_coord=random.randint(10,int(c.cget("width"))-width_of_ballon)#生成坐标
        y_coord=random.randint(int(c.cget("height"))-500,int(c.cget("height"))-height_of_ballon)#生成坐标
        list_of_balloons.append([x_coord,y_coord])
    while determine_overlap(list_of_balloons,true_or_false)==True:
        list_of_balloons.clear()
        for i in range (number_of_balloons):
            x_coord=random.randint(10,int(c.cget("width"))-width_of_ballon)#生成坐标
            y_coord=random.randint(int(c.cget("height"))-500,int(c.cget("height"))-height_of_ballon)#生成坐标
            list_of_balloons.append([x_coord,y_coord])
        print (list_of_balloons)
        print (determine_overlap(list_of_balloons,true_or_false))
    return list_of_balloons

def determine_overlap(list_of_coords, is_overlap):
    #排除所有重叠可能性
    is_overlap=False
    for index_of_main_balloon,compared_balloon_coords in enumerate(list_of_coords):  
        for index_of_minor_balloons,coords in enumerate(list_of_coords):
            right_side_x_coord_test_balloon=coords[0]+width_of_ballon
            right_side_x_coord_compared_balloon=compared_balloon_coords[0]+width_of_ballon
            lower_side_y_coord_test_balloon=coords[1]+height_of_ballon
            lower_side_y_coord_compared_balloon=compared_balloon_coords[1]+height_of_ballon
            
            if compared_balloon_coords[0]<=right_side_x_coord_test_balloon and\
            right_side_x_coord_compared_balloon>=coords[0] and\
            lower_side_y_coord_compared_balloon>=coords[1] and \
            compared_balloon_coords[1]<=lower_side_y_coord_test_balloon and index_of_main_balloon!=index_of_minor_balloons:
            
                is_overlap=True
                return is_overlap
        # if is_overlap==True:
        #     return is_overlap
    return is_overlap

        # if coords==compared_balloon_index:    
        #     break
        # if len(balloons_coords)>=number_of_balloons:
        #     balloons_coords.clear()
        # for i in range(number_of_balloons):
        #     generate_x_y()

balloons_coords=generate_x_y()
for latitude in range (6):#飞多高
    for index_of_balloons in range(number_of_balloons):#生成几个气球
        oval=c.create_oval(balloons_coords[index_of_balloons][0],balloons_coords[index_of_balloons][1],\
                        balloons_coords[index_of_balloons][0]+width_of_ballon,balloons_coords[index_of_balloons][1]+height_of_ballon,\
                        fill="red")#生成气球
        c.pack()
    print (balloons_coords)
    # for balloons in balloons_coords:
    #移动气球
    #     if latitude%2>0:
    #         balloons[0]-=10
    #     else:
    #         balloons[0]+=10
    #     balloons[1]-=latitude*1
    # c.update()
    # time.sleep(0.5)
    # c.delete("all")

# print (balloons_coords)

c.mainloop()