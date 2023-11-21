import tkinter as tk

my_book=tk.Tk()
my_book.title('我的画本')
c=tk.Canvas(my_book,width=800,height=400,)

c.create_oval(150,250,250,350)

c.pack()
c.update()
c.mainloop()