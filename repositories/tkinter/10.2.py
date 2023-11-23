'''
10-th homework 2nd question
基于tkinter画出如该链接所示图案：https://github.com/bochengjiang/python_class/blob/main/homework/image/10.2.png
'''

from tkinter import *

my_book=Tk()
c=Canvas(my_book,width=800,height=400,)

c.create_oval(10,10,30,30)#画脑袋
c.create_line(20,30,20,60,width=2)#画身体
c.create_line(19,30,5,45,width=1)#画左手
c.create_line(21,30,35,45,width=1)#画右手
c.create_line(18,60,5,90,width=1)#画左腿
c.create_line(21,60,35,90,width=1)#画右腿

c.pack()
c.update()
c.mainloop()