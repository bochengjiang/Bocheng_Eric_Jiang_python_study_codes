import random

point_player_1=0
point_player_2=0
i=1

while point_player_1<30 and point_player_2<30 and i<15:
    answer=int(random.randint(1,10))
    guess_1=input("玩家一请输入你的猜想：")
    guess_2=input("玩家二请输入你的猜想：")
    point_will_get = random.random()
    i=i+1

    if int(guess_1)==0 and int(guess_2)==0:
        break
        
    if point_will_get <=0.5:
        plus_number=2
    elif point_will_get<=0.75:
        plus_number=1
    else:
        plus_number=0
    
    if abs(answer-int(guess_1))<abs(answer-int(guess_2)):
        point_player_1=point_player_1+plus_number

    elif abs(answer-int(guess_2))<abs(answer-int(guess_1)):
        point_player_2=point_player_2+plus_number

    print ("玩家一得分："+str(point_player_1),"玩家二得分："+str(point_player_2))
    print ("正确答案："+str(answer))
    print (point_will_get)
