import random

lucky_number = random.randint(1,50)
guess=input("请输入你的答案：")
while int(guess) != lucky_number:
    #guess = input("请输入你的答案：")
    if lucky_number < int(guess):
        print("it is too big")
    elif lucky_number > int(guess):
        print("its too small")
    guess = input("请输入你的答案：")
print("good job")


