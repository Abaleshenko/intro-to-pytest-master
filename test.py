import turtle
from time import *


turtle.bgcolor("darkslateblue")
turtle.speed(0)
turtle.hideturtle()

x, y = -355, -49
coordinates = ((x, y),
               (x + 132, y + 3),
               (x + 223, y - 52),
               (x + 328, y - 103),
               (x + 343, y - 189),
               (x + 472, y - 210),
               (x + 502, y - 122))


def ursa_major(i, j):
    for k in range(7):
        turtle.color("yellow")
        turtle.forward(i)
        turtle.right(j)


for i in coordinates:
    turtle.penup()
    turtle.setpos(i)
    turtle.pendown()
    ursa_major(5, 144)


outline = turtle.Turtle()
outline.hideturtle()
outline.penup()

for i in coordinates:
    outline.goto(i)
    outline.color("red")
    outline.pendown()

outline.goto(coordinates[-4])
sleep(5)
