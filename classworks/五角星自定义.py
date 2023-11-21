import turtle

t=turtle.Pen()

def draw_star(length,color):
    t.color(color)
    left_angle = 120
    right_angle = 48
    for i in range (5):
        t.forward(length)
        t.left(left_angle)
        t.forward(length)
        t.right(right_angle)
        
draw_star(200,"purple")