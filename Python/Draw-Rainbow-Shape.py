# by using turtle module

import turtle

turtle.bgcolor("black")
turtle.speed(0)
turtle.pensize(2)

for i in range(15):
    for colours in ['red','magenta','blue','cyan','green','yellow','white']:
        turtle.color(colours)
        turtle.left(10)
        turtle.forward(10)
        turtle.left(10)
        turtle.forward(10)
        turtle.right(20)
        turtle.forward(50)
        turtle.right(140)
        turtle.forward(50)
        turtle.right(20)
        turtle.forward(10)
        turtle.left(10)
        turtle.forward(10)
        turtle.left(170)
