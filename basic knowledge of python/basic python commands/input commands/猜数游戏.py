import random

lucky_number = random.randint(1,50)
#correct_number = 0
#guess=input("请输入你的答案：")
while True:       #int(guess) != lucky_number:
    guess = input("请输入你的答案：")
    if lucky_number < int(guess):
        print("it is too big")
    elif lucky_number > int(guess):
        print("its too small")
    else:
        print("good job")
        break
        #correct_number = correct_number+1

