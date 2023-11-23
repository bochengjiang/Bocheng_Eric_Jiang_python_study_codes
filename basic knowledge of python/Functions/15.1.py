'''
15-th homework 1st question
当输入 1 时，小海龟前进 100
输入 2 时，小海龟左转 90 度
输入 3 时，小海龟右转 90 度
输入 4 时，小海龟变成红色
输入 5 时，小海龟变成绿色
输入 6 时，小海龟在当前位置画一个正方形
输入 7 时，小海龟把画笔的线宽调成 5
可参考该相对路径所示动画："homework/image/15.1.gif"

预估完成时长:60 - 120 min
实际：4h
'''

import turtle
import copy

turtle_list=[]
turtle_green_color_data=["#007500","#009100","#00A600","#00BB00","#00DB00","#00EC00",\
                         "#28FF28","#53FF53","#79FF79","#93FF93","#A6FFA6","#BBFFBB"]
turtle_red_color_data=["#600000","#750000","#930000","#AE0000","#CE0000","#EA0000",\
                       "#FF0000","#FF2D2D","#FF5151","#FF7575","#FF9797","#FFB5B5"]
turtle_blue_color_data=["#0000C6","#0000C6","#0000E3","#2828FF","#4A4AFF","#6A6AFF",\
                        "#7D7DFF","#9393FF","#AAAAFF","#B9B9FF","#CECEFF","#DDDDFF"]

for i in range(12):
    turtle_list.append(turtle.Turtle(shape="turtle"))

def move_turtle(list_obj):
    temp_turtle_list=list_obj.copy()
    while len(temp_turtle_list)>0:
        for index,each_turtle in enumerate(temp_turtle_list):
            each_turtle.color(turtle_blue_color_data[index])
            each_turtle.pu()
            each_turtle.fd(25)
            each_turtle.lt(180-(len(turtle_list)*180-360)/len(turtle_list))
        temp_turtle_list.pop(index)
        
move_turtle(turtle_list)

def draw_polygon(number_of_sides, edge_length):
    for turtles in turtle_list:
        for i in range (number_of_sides):
            turtles.fd(edge_length)
            turtles.lt(180-(number_of_sides*180-360)/number_of_sides)

for each_turtle in turtle_list:
    each_turtle.pd()

def press_1():
    for each_turtle in turtle_list:
        each_turtle.fd(100)
def press_2():
    for each_turtle in turtle_list:
        each_turtle.lt(90)
def press_3():
    for each_turtle in turtle_list:
        each_turtle.rt(90)
def press_4():
    for index,each_turtle in enumerate(turtle_list):
        each_turtle.color(turtle_red_color_data[index])
def press_5():
    for index,each_turtle in enumerate(turtle_list):
        each_turtle.color(turtle_green_color_data[index])
# def press_6():
#     draw_polygon(number_of_sides,side_length)
def press_7():
    for each_turtle in turtle_list:
        each_turtle.width(5)

while True:
    user_answer=input("请输入一个数字或指令：")
    if user_answer=="1":
        press_1()
    elif user_answer=="2":
        press_2()
    elif user_answer=="3":
        press_3()
    elif user_answer=="4":
        press_4()
    elif user_answer=="5":
        press_5()
    elif user_answer=="6":
        number_of_sides=int(input("几条边："))
        side_length=int(input("多宽："))
        draw_polygon(number_of_sides,side_length)
    elif user_answer=="7":
        press_7()
    else:
        print("程序结束")
        break
    

turtle.done()