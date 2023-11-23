# 9-th homework 1st question
'''
用尽可能简洁的代码，使得代码输出结果为：
100
100 110
100 110 120
100 110 120 130
100 110 120 130 140
'''
for i in range (6):#循环输出多少行
    data_in_row=list(range(100,100+10*i,10))#创建决定每排内容的列表
    for data in data_in_row: #小循环，输出一排的内容
        print (data,end=" ")#输出一排单个的内容
    print(end="\n")#每排输出后换行