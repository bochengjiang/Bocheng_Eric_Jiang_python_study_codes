import random

vote_number=0
super_hero_votes=[0,0,0]
super_hero = ["Ironman:","Cap:","Hulk:"]
while vote_number<100: 
    vote=random.randint(0,2)
    vote_number+=1
    super_hero_votes[vote]+=1
    super_hero= ["Ironman:"+str(super_hero_votes[0]),"Cap:"+str(super_hero_votes[1]),"Hulk:"+str(super_hero_votes[2])]
    print(super_hero)

