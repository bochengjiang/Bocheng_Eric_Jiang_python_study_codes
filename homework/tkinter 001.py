import tkinter as tk
from tkinter import simpledialog,messagebox

#simpledialog.Dialog(my_book)
#answer=messagebox.askyesno(title="酒驾检测",message="你开车前是否喝过酒")
#if answer == True:
    #messagebox.showwarning(title="请不要酒驾",message="开车不喝酒，喝酒不客车，请您立刻下车")
#else:
    #messagebox.showinfo(title="", message="祝您一路顺风")

user_answer=False

while user_answer==False:
    number_of_rectangle=simpledialog.askinteger("长方形数量","请输入长方形的数量(整数)")
    rectangle_height=simpledialog.askinteger("长方形高","请输入长方形的高(整数)")
    rectangle_width=simpledialog.askinteger("长方形款","请输入长方形的款(整数)")
    rec_color_fill=simpledialog.askstring("矩形填充颜色","想用什么颜色填充矩形")
    rec_color_outline=simpledialog.askstring("矩形边框颜色","想用什么颜色作为矩形的边框")
    #user_answer=messagebox.askyesno(title="确认信息",message="请确认一下信息: 长方形数量为:"+str(number_of_rectangle)+\
    #"长方形高为:"+str(rectangle_height)+"长方形的宽为"+str(rectangle_width)+"长方形填充的颜色为:"+rec_color_fill+\
    #"长方形边线的颜色:"+rec_color_outline)
    user_answer=messagebox.askyesno(title="确认信息",\
    message=f"请确认以下以信息：矩形的数量：{number_of_rectangle} 矩形的宽为：{rectangle_width} \
    矩形的高得：{rectangle_height} 填充的颜色：{rec_color_fill} 边的颜色：{rec_color_outline}")
my_book=tk.Tk()
my_book.title('我的画本')
c=tk.Canvas(my_book,width=800,height=400,)

bigger_x=20+rectangle_width
smaller_x=20
for i in range (number_of_rectangle):
    c.create_rectangle(smaller_x,20,bigger_x,20+rectangle_height,\
    fill=rec_color_fill,outline=rec_color_outline)
    smaller_x=bigger_x
    bigger_x=bigger_x+rectangle_width

c.pack()
c.update()
c.mainloop()