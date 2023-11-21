'''
11-th homework 2nd question
画出如该相对路径所示动画："homework/image/11.2.gif"
'''

from tkinter import *
import time

win=Tk()
c=Canvas(win, width=500,height=500)

blue=c.create_rectangle(0,0,10,10,fill="blue",outline="blue")
yellow=c.create_rectangle(490,490,500,500,fill="yellow",outline="yellow")

for i in range (245):
    c.move(blue,1,1)
    c.move (yellow,-1,-1)
    c.pack()
    c.update()
    time.sleep(0.01)

c.create_rectangle(245,245,255,255,fill="green",outline="green")

c.pack()
c.update()
c.mainloop()
