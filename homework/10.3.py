'''
10-th homework 3rd question
用tkinter展示一个矩形从画布的左上角移动到右下角的动画。
'''
from tkinter import *
import time

my_book=Tk()
c=Canvas(my_book,width=1000,height=800)

squ=c.create_rectangle(40,70,60,90)
for i in range (200):
    c.move(squ,(980-40)/200,(780-70)/200)
    c.pack()
    c.update()
    time.sleep(0.1)

c.mainloop()






