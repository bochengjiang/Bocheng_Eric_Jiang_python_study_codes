def my_range(start,end,step=1):
    my_list=[]
    if step>0:
        #向my_list中传入start到end(不含end)之间的数（每隔step个）
        while start < end:
            my_list.append(start)
            start=start+step
    else:#step==0 或者 step为负数
        #向my_list中传入数据直到start<=end
        while start>end:
            my_list.append(start)
            start = start+step
    return my_list

numberlist=my_range(0,-10)
number_list_2=range(0,-10)
print(numberlist)
print(list(number_list_2))