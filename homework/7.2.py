# 7-th homework 2st question
## There are six little monsters in monsters. 
## After a hero kills a little monster at random, the monster is removed from the monsters list, 
## and the name of the little monster is printed at the same time until the length of the monsters list is 0.
import random
monsters = ["m0", "m1", "m2", "m3", "m4", "m5"] 
while len(monsters)>0:
    monster_killed_index=random.randint(0,len(monsters)-1)
    print(monsters[monster_killed_index])
    monster_name=monsters[monster_killed_index]
    #monsters.pop(monster_killed_index)
    del monsters[monster_killed_index]
    print(monsters)