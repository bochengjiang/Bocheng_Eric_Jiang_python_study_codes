'''
11-th homework 4th question
画出如该相对路径所示动画："homework/image/11.4.1.GIF"
如该动画效果完成好，可挑战:"homework/image/11.4.2.GIF"
'''
from tkinter import *
import time

win=Tk()
c=Canvas(win,width=1000,height=1000)

million_confused_face=[]

img_file=PhotoImage(file="image\confused.gif")
smaller_img=img_file.subsample(3,3)
for i in range (10):
    for x in range (10):
        confused_face=c.create_image(smaller_img.width()*x+50,smaller_img.height()*i+60,anchor="nw",image=smaller_img)
        million_confused_face.append(confused_face)
        c.pack()
        c.update()
        time.sleep(0.1)
        for y in million_confused_face:
            c.move(y,1,0)