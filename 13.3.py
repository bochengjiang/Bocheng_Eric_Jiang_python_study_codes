'''
13-th homework 3rd question
制作阶乘函数并调用
函数名为 factorial，参数只有一个。
例如 factorial(9)的效果为求 9 的阶乘

预估完成时长：10 - 30 min
实际:51min
'''

from tkinter import *
from tkinter import simpledialog,messagebox

win=Tk()

def Factorial(number_factored):
    number=number_factored
    number_factored_list=[]
    for i in range (number_factored):
        if number<1:
            break
        number_factored_list.append(number)
        number-=1
    for i in range(len(number_factored_list)-1):
        multiple_1=number_factored_list[i]
        multiple_2=number_factored_list[i+1]
        if i>=1:
            final_result=final_result*multiple_2
        else:
            final_result=multiple_1*multiple_2
    print (final_result)
    return final_result

factorial_number=simpledialog.askinteger("factorial_number","请输入想要阶乘的数字")

result=Factorial(factorial_number)

messagebox.showinfo("阶乘结果",f"您输入的数字为{factorial_number},结果为{result}")
