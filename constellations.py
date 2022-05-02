import turtle

turtle.bgcolor("darkslateblue")   # darkslateblue
turtle.speed(0)
turtle.hideturtle()

x = -350
y = -50
coordinates = ((x, y),
               (x + 135, y + 1),
               (x + 220, y - 50),
               (x + 330, y - 105),
               (x + 344, y - 188),
               (x + 470, y - 209),
               (x + 500, y - 123))


def ursa_major(i, j):
    for k in range(7):
        turtle.color("yellow")
        turtle.forward(i)
        turtle.right(j)


def star_connect():
    for i in range(1):
        ursa_major(5, 144)


for i in coordinates:
    turtle.penup()
    turtle.setpos(i)
    turtle.pendown()
    star_connect()

my = turtle.Turtle()
my.hideturtle()
my.penup()

for i in coordinates:
    my.goto(i)
    my.color("red")
    my.pendown()

my.goto(coordinates[-4])
