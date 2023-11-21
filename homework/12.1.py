'''
12-th homework 1st question
在11.3.py的代码的基础上进行优化，相关图片可以在homework/image/chess里面找到
要求：有棋盘，每个棋子显示对应的图片，代码尽可能地避免重复
'''

from tkinter import *

win=Tk()
c=Canvas(win,width=800,height=800)

def draw_chess_board_row(line_index):
    x=0
    while x<=7:
        if (line_index+x)%2>0:
            color="white"
        else:
            color="grey" 
        c.create_rectangle(x*100,line_index*100,(x+1)*100,(line_index+1)*100,fill=color)
        x+=1


def odd_number_row(y):
    for x in range (8):
        if (x+1)%2>0:#根据x的值判断象棋盘上的格子颜色
            color="white"
        else:
            color="grey"
        c.create_rectangle(x*100,y*100,(x+1)*100,(y+1)*100,fill=color)

def even_number_row(line_index):
    for x in range (8):
        if x%2>0:#根据x的值判断象棋盘上的格子颜色
            color="white"
        else:
            color="grey"
        c.create_rectangle(x*100,line_index*100,(x+1)*100,(line_index+1)*100,fill=color)

#创建国际象棋板
for y in range(8):
    # if (y+1)%2>0:
    #     odd_number_row(y)
    # else:
    #     even_number_row(y)
    draw_chess_board_row(y)

black_chess_peice=["homework\image\chess\\bishop_black.png","homework\image\chess\king_black.png",
                   "homework\image\chess\knight_black.png","homework\image\chess\pawn_black.png",
                   "homework\image\chess\queen_black.png","homework\image\chess\\rook_black.png"]
img_files={}

#导入文件

for i,location in enumerate(black_chess_peice):
    x=PhotoImage(file=location)
    img_files[i]=x


print(img_files)

#1.1.1
pawns_name_list=["bp1","bp2","bp3","bp4","bp5","bp6","bp7","bp8"]
all_black_pawns=dict.fromkeys(pawns_name_list)

for i,pawn_name in enumerate(pawns_name_list):
    pawns_return_value=c.create_image(i*100+50,150,anchor="center", image=img_files[3])
    all_black_pawns[pawn_name]=pawns_return_value

print (all_black_pawns)

    

c.pack()
c.update()
c.mainloop()
