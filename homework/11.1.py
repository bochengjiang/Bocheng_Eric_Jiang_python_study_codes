'''
11-th homework 1st question
画出如该相对路径所示动画："homework/image/11.1.GIF"
'''
from tkinter import *
import time

win=Tk()
c=Canvas(win,width=800, height=200)

colors=["red","orange","yellow","green","cyan","blue","purple"]

i=0
def draw_circle(small_x_coord,big_x_coord,fill_color):
    c.create_oval(small_x_coord,50,big_x_coord,150,fill=fill_color,width=15)#绘画单个填充了不同颜色的圆形
    c.pack()
    c.update()
    time.sleep(0.05)

for a in range (2): #重复1次半给七个圆形填充颜色然后再删除
# 绘制七个不同颜色的圆形
    while i<7:
        draw_circle(i*100+50,(i+1)*100+50,colors[i%7])
        i+=1
    #在第二次循环时循环到此为止
    if a==1:
        break
    #将7个圆形填充的颜色依次换为黑色（从左手边开始）
    for x in range (7):
        # c.create_oval(x*100+50,50,(x+1)*100+50,150,fill="black",width=15)#画黑色圆形
        # c.pack()
        # c.update()
        #time.sleep(0.05)
        draw_circle(x*100+50,(x+1)*100+50,"black")   
    i=0
    time.sleep(0.05)

i=6
##将7个圆形填充的颜色依次换为黑色（从右手边开始）
while i>=0:
    # c.create_oval(i*100+50,50,(i+1)*100+50,150,fill="black",width=15)#画黑色圆形
    # c.pack()
    # c.update()
    # time.sleep(0.1)
    draw_circle(i*100+50,(i+1)*100+50,"black")
    i-=1

#29-35: 同时闪烁彩虹颜色的圆形三次
for a in range (3):
    #画出七个彩虹色的圆形（同时显示）
    i=0
    while i<7:
        c.create_oval(i*100+50,50,(i+1)*100+50,150,fill=colors[i%7],width=15)#绘画单个填充了不同颜色的圆形
        i+=1
    c.pack()
    c.update()
    time.sleep(0.1)
    #将7个圆形填充的颜色换为黑色（同时显示）
    for x in range (7):
        c.create_oval(x*100+50,50,(x+1)*100+50,150,fill="black",width=15)#画黑色圆形
    c.pack()
    c.update()
    time.sleep(0.1)

#每一个圆形都统一依次闪烁彩虹中的颜色重复七次
for a in range (7):
    #画出七个彩虹色的圆形（同时显示）
    i=0
    while i<7:
        c.create_oval(i*100+50,50,(i+1)*100+50,150,fill=colors[a%7],width=15)#绘画单个填充了不同颜色的圆形
        i+=1
    c.pack()
    c.update()
    time.sleep(0.1)
    #将7个圆形填充的颜色换为黑色（同时显示）
    for x in range (7):
        c.create_oval(x*100+50,50,(x+1)*100+50,150,fill="black",width=15)#画黑色圆形
    c.pack()
    c.update()
    time.sleep(0.1)

#从第一个圆形开始，每一个单独闪烁彩虹中的颜色，整个过程重复两遍
for x in range (2):
    i=0
    while i<7:
        #是特定的圆形亮起
        c.create_oval(i*100+50,50,(i+1)*100+50,150,fill=colors[i%7],width=15)#绘画单个填充了不同颜色的圆形
        c.pack()
        c.update()
        time.sleep(0.1)
        #是同样一个圆形灭掉
        c.create_oval(i*100+50,50,(i+1)*100+50,150,fill="black",width=15)#画黑色圆形
        #改变i
        i+=1
