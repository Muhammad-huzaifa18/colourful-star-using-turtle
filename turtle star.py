from turtle import *
setup()
t1 = Turtle()
colors = ["red" , "blue"  , "yellow" , "orange" ,]
import random

t1.up()
t1.goto(-200,10)
t1.down()
t1.width(4)
t1.hideturtle()
for i in range(12):
    colorchoice = random.choice(colors)
    t1.color(colorchoice)
    t1.forward(400)
    t1.right(150)
    t1.speed(10)
