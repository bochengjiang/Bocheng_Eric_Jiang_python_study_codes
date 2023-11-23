'''
13-th homework 2nd question
制作小海龟电子钟倒计时函数并调用
函数名：countdown，参数仅一个。
如 countdown（10）的效果为小海龟电子钟倒计时10秒钟。

预估完成时长：10 - 30 min
实际：12min
'''

import turtle 
import time 

t=turtle.Pen()
t.hideturtle()

def turtle_countdown(second):
    seconds=second
    for i in range (seconds):
        t.write(seconds,align="center")
        seconds=seconds-1
        time.sleep(1)
        t.clear()

turtle_countdown(10)