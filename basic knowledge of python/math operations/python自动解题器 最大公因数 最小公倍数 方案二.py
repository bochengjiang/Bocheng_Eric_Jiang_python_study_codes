number_1 = int(input("输入第一个数字："))
number_2 = int(input("输入第二个数字："))
number =1
if number_1 > number_2:
    number = number_2
else:
    number = number_1
    
while number_2%number!=0 or number_1%number!=0:
    number=number-1
number_1 = number_1/number
number_2=number_2/number
LCM=int(number*number_1*number_2)
print("最大公因数为："+str(number))
print("最小公倍数为："+str(LCM))
