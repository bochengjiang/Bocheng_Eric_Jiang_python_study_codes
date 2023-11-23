# 7-th homework 3rd question
## 小海龟挖完矿后，准备把换得的金币随机地埋在十个不同的地方。
## 一个月黑风高的夜晚，小明得知了小海龟的藏金处，并准备每个洞偷走10个金币。
## 要求：需要记录各个地方存储的金币数量和变化
import random,copy

gold_hiding_place=[[],[],[],[],[],[],[],[],[],[]]

i=0
while len(gold_hiding_place[9])<=15:
    number=random.randint(10,100)
    gold_hiding_place[i%10].append(number)
    i=i+1

i=0
while len(gold_hiding_place[9])>5:
    money_stole_index=random.randint(0,len(gold_hiding_place[i%10])-1)
    org_gold_hiding_place=copy.deepcopy(gold_hiding_place[i%10])
    #print(i,"old：",gold_hiding_place[i%10],)
    gold_hiding_place[i%10].pop(money_stole_index)
    print(i%10,"now:",gold_hiding_place[i%10],"old:",org_gold_hiding_place)
    i=i+1