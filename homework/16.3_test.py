true_or_false=False
yes_no_break=False
def determine_overlap(list_of_coords, change):
    #排除所有重叠可能性
    global yes_no_break
    for index_of_main_balloon,compared_balloon_coords in enumerate(list_of_coords):  
        for index_of_minor_balloons,coords in enumerate(list_of_coords):
            right_side_x_coord_test_balloon=coords[0]+width_of_ballon
            right_side_x_coord_compared_balloon=compared_balloon_coords[0]+width_of_ballon
            lower_side_y_coord_test_balloon=coords[1]+height_of_ballon
            lower_side_y_coord_compared_balloon=compared_balloon_coords[1]+height_of_ballon
            
            if compared_balloon_coords[0]<=right_side_x_coord_test_balloon and\
            right_side_x_coord_compared_balloon>=coords[0] and\
            lower_side_y_coord_compared_balloon>=coords[1] and \
            compared_balloon_coords[1]<=lower_side_y_coord_test_balloon and index_of_main_balloon!=index_of_minor_balloons:
            
                yes_no_break=True
                change=True
        if yes_no_break==True:
            return change
    return change

height_of_ballon=100
width_of_ballon=100

#测试案例1=True, =true
test_1=[[0,0],[9,9]]
#测试案例2=True, =true
test_2=[[0,0],[0,0]]
#测试案例3=True, =true
test_3=[[0,0],[10,0]]
#测试案例4=True, =true
test_4=[[0,0],[0,10]]
#测试案例5=True, =true
test_5=[[30,30],[30,30],[90,90]]
#测试案例6=False, =False
test_6=[[0,0],[100,100]]

#测试案例7=True
test_7=[[598, 571], [496, 848], [109, 678], [36, 774]]
test_8=[[537, 887], [506, 860]]

test_9=[[356, 649], [505, 616], [780, 627], [880, 632], [892, 510], [362, 805]]

all_tests=[test_1,test_2,test_3,test_4,test_5,test_6]

#for tests in all_tests:
for i in range (2):
    a=determine_overlap(test_9, true_or_false)
    print (a)