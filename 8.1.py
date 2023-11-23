# 8-th homework 1st question
## Step1: 5个小怪兽，它们的名字储存在列表name中，它们的血量储存在hp列表中。请补充下面的代码，使得代码输出的结果为：
'''
Jim 's hp is 8
Tim 's hp is 3
Eve 's hp is 10
Tom 's hp is 6
Lynn 's hp is 5
'''
## Step2: 绿巨人从怪兽列表中随机挑选一个小怪兽攻击，小怪兽被攻击后丧失一滴血量。（此过程重复25次）
## Step3: 但是小怪兽们都长得太像了，每次攻击过后，不知道各个小怪兽血量还剩多少。我们应该怎么帮助他呢？

#step 1
name=["Jim","Tim","Eve","Tom","Lynn"]
hp=[8,3,10,6,5]

#step 2
import random
for i in range (25):
    monster_index=random.randint(0,4)
    hp[monster_index]=hp[monster_index]-1
    if hp[monster_index] <= 0:
        hp[monster_index]=0
    print(name[monster_index],":",hp[monster_index])
print (name, hp)