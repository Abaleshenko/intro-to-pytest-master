import turtle
a = 0
b = 0

turtle.bgcolor("gray10")
turtle.speed(0)
turtle.pencolor("dark green")
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()

while True:
    turtle.forward(a)
    turtle.right(b)
    a += 3
    b += 1


