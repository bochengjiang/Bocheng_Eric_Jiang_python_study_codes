from tkinter import *
#from PIL import Image,ImageTk

win=Tk()
c=Canvas(win,width=1000,height=1000)

img_file=PhotoImage(file="homework\image\confused.gif")
smaller_img=img_file.subsample(3,3)
for i in range (10):
    for x in range (10):
        c.create_image(smaller_img.width()*x+50,smaller_img.height()*i+60,anchor="nw",image=smaller_img)

c.pack()
c.update()
c.mainloop()