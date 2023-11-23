list_of_coords=[[579, 642], [110, 551], [106, 568], [403, 905], [891, 805], [44, 735], [727, 807], \
                [265, 829], [883, 770], [263, 600]]
height_of_ballon=90
width_of_ballon=50

for index_of_main_balloon,compared_balloon_coords in enumerate(list_of_coords):  
    for index_of_minor_balloons,coords in enumerate(list_of_coords):
        if compared_balloon_coords[0]<=coords[0]+width_of_ballon and\
        compared_balloon_coords[0]+width_of_ballon>=coords[0] and\
        compared_balloon_coords[1]+height_of_ballon>=coords[1] and \
        compared_balloon_coords[1]<=coords[1]+height_of_ballon and index_of_main_balloon!=index_of_minor_balloons:
            print("hi")
        else:
            print("bye")