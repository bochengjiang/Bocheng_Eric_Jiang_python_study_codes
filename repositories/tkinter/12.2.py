'''
12-th homework 2nd question
画出如该相对路径所示动画："homework/image/12.2.gif"
图片素材：
> homework/image/confused.gif
> homework/image/run.gif
'''

from tkinter import *
import time

win=Tk()
c=Canvas(win,height=1000,width=1000)

confused_faces=[]
run_emoji=[]

#导入照片
confused_img=PhotoImage(file="homework\image\confused.gif")
run_img=PhotoImage(file="homework\image\\run.gif")
#调整照片大小
smaller_confused=confused_img.subsample(4,4)

img_files=[smaller_confused,run_img]

def draw_two_lines(number_of_lines):
    x_cor=0
    for y_cor in range(number_of_lines):
        for x in range (5):
            img=c.create_image(x*smaller_confused.width()*2+150,\
                                y_cor*smaller_confused.height()+100,anchor="nw",image=img_files[x_cor%2])
            if x_cor%2>0:
                run_emoji.append(img)
            else:
                confused_faces.append(img)
            x_cor+=1

#创建整体图片
draw_two_lines(5)


#挪动每一个confused_face 和 run_emo
for i in range(100):
    for confused_face in confused_faces:
        c.move(confused_face,-1,1)
    for run_emo in run_emoji:
        c.move(run_emo,4,0)
    c.pack()
    c.update()
    time.sleep(0.05)