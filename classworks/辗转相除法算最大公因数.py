big_number=0
small_number=0
number_1=int(input("请输入第一个数字:"))
number_2=int(input("请输入第二个数字:"))
remainder=1

if number_1>number_2:
    big_number=number_1
    small_number=number_2
else:
    big_number=number_2
    small_number=number_1

while remainder!=0:
    remainder=big_number%small_number
    big_number=small_number
    small_number=remainder
    
print (big_number)