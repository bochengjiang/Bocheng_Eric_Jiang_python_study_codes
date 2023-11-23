'''
10-th homework 4th question
用tkinter在画布上贴上链接对应的图片：https://github.com/bochengjiang/python_class/blob/main/homework/image/confused.gif
'''
from tkinter import *

my_book=Tk()
my_book.title('我的画本')
c=Canvas(my_book,width=800,height=400,)

img_file=PhotoImage(file="homework\image\confused.gif")
c.create_image(10,10,anchor="nw",image=img_file)
c.create_text(50,250,anchor="nw",text="一脸茫然.gif",font=("",20))

c.pack()
c.update()
c.mainloop()
