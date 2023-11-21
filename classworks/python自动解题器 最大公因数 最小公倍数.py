number_1 = int(input("输入第一个数字："))
number_2 = int(input("输入第二个数字："))
final_result_number_1=0
final_reslut_number_2=0
GCF = 1
divided_number = 2

for i in range (10000):
    #judge what number can fully divide number_1 and number_2
    if number_1%divided_number==0 and number_2%divided_number==0:
        number_1=number_1/divided_number
        number_2=number_2/divided_number
        GCF = GCF*divided_number
    #else:
        #final_result_number_1=
    divided_number=divided_number+1
    if divided_number>=7:
        divided_number=2
    

print (GCF)


































        
