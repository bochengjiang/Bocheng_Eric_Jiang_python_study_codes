# 8-th homework 4th question
'''
用尽可能简洁的代码，使得代码输出结果为：
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
# i2=[]
# for i in range(5):
#     i2.append(i)
#     i=i+1
#     print (i2)

for i in range (5):#循环输出多少行
    data_in_row=list(range(3,5+2*i,2))#创建决定每排内容的列表
    for data in data_in_row: #小循环，输出一排的内容
        print (data,end=" ")#输出一排单个的内容
    print(end="\n")#每排输出后换行
        