import random
from tkinter import *

win=Tk()
c=Canvas(win,width=1000,height=1000)

height_of_ballon=100
width_of_ballon=100
number_of_balloons=10
true_or_false=False
width=1000
height=1000

balloons_coords=[]


#创建一个判断是否重叠的程序
def generate_x_y():
    list_of_balloons=[]
    for i in range (number_of_balloons):
        x_coord=random.randint(10,width-width_of_ballon)#生成坐标
        y_coord=random.randint(height-500,height-height_of_ballon)#生成坐标
        list_of_balloons.append([x_coord,y_coord])
    while determine_overlap(list_of_balloons,true_or_false)==True:
        list_of_balloons.clear()
        for i in range (number_of_balloons):
            x_coord=random.randint(10,width-width_of_ballon)#生成坐标
            y_coord=random.randint(height-500,height-height_of_ballon)#生成坐标
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

# generate_x_y()

balloons_coords=generate_x_y()

for balloons in balloons_coords:
    c.create_rectangle(balloons[0], balloons[1], balloons[0]+width_of_ballon, balloons[1]+height_of_ballon)

#true
# test=[[454, 896], [563, 576], [816, 695], [128, 826], [776, 726], [114, 558]]

# print(determine_overlap(test, true_or_false))

c.pack()
c.update()
c.mainloop()