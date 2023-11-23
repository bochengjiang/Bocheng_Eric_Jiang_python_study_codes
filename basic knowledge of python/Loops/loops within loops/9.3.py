'''
# 9-th homework 3rd question
用尽可能简洁的代码，画出以下图形（使得代码输出结果如下面所示）：
   *
  ***
 *****
*******
'''
space=6

for i in range (4):#循环输出多少行
   print (" "*space,end="")#
   for y in range (2*i+1): #小循环，输出一排的内容
      print ("*",end="")#输出一排单个的内容
   space=space-2
   print(end="\n") 

'''
      *
    ***
  *****
*******
'''