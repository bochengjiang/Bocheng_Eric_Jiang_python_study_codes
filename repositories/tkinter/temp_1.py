from tkinter import *
import time

my_book=Tk()
c=Canvas(my_book,width=1000,height=800)

cir=c.create_oval(90,180,95,185)

c.pack()
c.update()
time.sleep(3)

c.move(cir,100,-150)


c.pack()
c.update()
c.mainloop()