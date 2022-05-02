import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('orange')
t.speed(12)

for i in range(100):
    t.circle(190, 90)
    t.lt(98)
    t.circle(190, 90)
    t.lt(18)

