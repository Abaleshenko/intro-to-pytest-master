import turtle

# SQUARE DRAW
"""

wn = turtle.Screen()
wn.bgcolor("yellow")
wn.title("Turtle")

skk = turtle.Turtle()  # Экземпляр класса

for i in range(4):
    skk.width(3)  # Толщина линии
    skk.color("green")  # Установить цвет
    skk.forward(100)  # Переместить перо на 100 пикселей
    skk.left(90)  # Повернуть влево перо на 90 градусов

turtle.done()
"""

# POLYGONS DRAW
polygon = turtle.Turtle()
w = turtle.Screen()

w.bgcolor("azure")
polygon.pencolor("bisque3")
w.title("Polygon")
polygon.goto(0, 120)
polygon.clear()

num_sides = int(input("Введите количество сторон полигона: 3, 5, 6 и далее: "))
side_length = 150
angle = 360.0 / num_sides
polygon.width(3)

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()