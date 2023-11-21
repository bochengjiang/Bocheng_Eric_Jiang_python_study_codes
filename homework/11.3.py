'''
11-th homework 3rd question
使用tkinter绘制国际棋盘，并使之具备下棋功能（棋子显示在用户指定区域）。
提示：可以先写出伪代码
'''
from tkinter import *
from tkinter import simpledialog
import time

win=Tk()
c=Canvas(win,width=800,height=800)

for y in range (8):
    for x in range (8):
        c.create_rectangle(x*100,y*100,(x+1)*100,(y+1)*100)

Bs1=c.create_text(50,150,text="Bs1",anchor="center",font=("",30))
Bs2=c.create_text(150,150,text="Bs2",anchor="center",font=("",30))
Bs3=c.create_text(250,150,text="Bs3",anchor="center",font=("",30))
Bs4=c.create_text(350,150,text="Bs4",anchor="center",font=("",30))
Bs5=c.create_text(450,150,text="Bs5",anchor="center",font=("",30))
Bs6=c.create_text(550,150,text="Bs6",anchor="center",font=("",30))
Bs7=c.create_text(650,150,text="Bs7",anchor="center",font=("",30))
Bs8=c.create_text(750,150,text="Bs8",anchor="center",font=("",30))

Bc1=c.create_text(50,50,text="Bc1",anchor="center", font=("",30))
Bc2=c.create_text(750,50,text="Bc2",anchor="center", font=("",30))

Bh1=c.create_text(150,50,text="Bh1",anchor="center", font=("",30))
Bh2=c.create_text(650,50,text="Bh2",anchor="center", font=("",30))

Bkn1=c.create_text(250,50,text="Bkn1",anchor="center", font=("",30))
Bkn2=c.create_text(550,50,text="Bkn2",anchor="center", font=("",30))

Bk=c.create_text(450,50,text="Bk",anchor="center", font=("",30))
Bq=c.create_text(350,50,text="Bq",anchor="center", font=("",30))

c.pack()
c.update()

local_dict=locals()

for i in range (1):
    name=simpledialog.askstring(title="挪动的棋",prompt="请问要挪动哪个棋子 (ex. Bs1)")
    x_cor=simpledialog.askinteger(title="x坐标",prompt=f"想把{name}挪动到什么地点，请填入x坐标(0<x<=8)")
    y_cor=simpledialog.askinteger(title="y坐标",prompt=f"想把{name}挪动到什么地点，请填入y坐标(0<y<=8)")
    name_coords=c.coords(local_dict[name])
    name_x=name_coords[0]
    name_y=name_coords[1]
    c.move(local_dict[name],x_cor*100-50-name_x,y_cor*100-50-name_y)
c.mainloop()