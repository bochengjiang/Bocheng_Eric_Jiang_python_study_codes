import turtle
import random

# 设置Turtle
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Balloons")

# 定义气球列表和颜色列表
balloons = []
colors = ["red", "blue", "green", "purple", "orange", "yellow", "pink"]

# 创建气球类
class Balloon(turtle.Turtle):
    def __init__(self, color):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.shapesize(stretch_wid=2, stretch_len=2)  # 设置气球大小
        self.penup()

# 检查新位置是否与其他气球重叠
def check_overlap(x, y):
    for balloon in balloons:
        if abs(x - balloon.xcor()) < 60 and abs(y - balloon.ycor()) < 60:
            return True
    return False

# 随机生成7个气球
for _ in range(7):
    color = random.choice(colors)
    balloon = Balloon(color)
    x, y = random.randint(-300, 300), random.randint(-200, -100)  # 修改初始位置为从下到上
    while check_overlap(x, y):
        x, y = random.randint(-300, 300), random.randint(-200, -100)
    balloon.goto(x, y)
    balloons.append(balloon)

# 气球摇晃上升
for _ in range(100):
    for balloon in balloons:
        balloon.sety(balloon.ycor() + random.randint(1, 5))
        balloon.setx(balloon.xcor() + random.randint(-3, 3))

# 保持窗口打开
turtle.done()