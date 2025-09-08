import turtle
import random
def Draw(x,y,r,c):
    t.penup()
    t.goto(x,y-r)
    t.pendown()
    t.color(c)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

t = turtle.Pen()
for i in range(10):
    data=[]
    x,y=random.randint(-200,200),random.randint(-200,200)
    r=random.randint(10,50)
    c=random.choice(["red","green","blue","black"])
    data.append((x,y,r,c))
    Draw(x,y,r,c)
    print(data)

turtle.done()
