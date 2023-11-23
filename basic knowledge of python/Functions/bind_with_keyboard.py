from tkinter import *

win=Tk()
c=Canvas(win,width=1000, height=1000)

c.pack()

def right(event):
    c.move(obj,10,0)
    c.update()

obj=c.create_rectangle(10,0,20,10)
c.update()
c.bind_all("<Right>",right)
c.mainloop()