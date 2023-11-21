'''
13-th homework 4th question
制作多边形函数并调用
参数只有两个，一个是边数，一个是边长。

预估完成时长：20 - 45 min
实际：16min

'''
import turtle
t=turtle.Pen()
t.hideturtle()

def draw_polygon(number_of_sides, edge_length):
    for i in range (number_of_sides):
        t.fd(edge_length)
        t.lt(180-(number_of_sides*180-360)/number_of_sides)

draw_polygon(75,100)