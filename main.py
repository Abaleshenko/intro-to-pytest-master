
all([49 // 7 != 1,
     "🍕" in "hello",
     8 == 8])






colors = ['black', 'white']
sizes = ['🍕', '🧺', 'L']

tshirts = [(color, size) for color in colors for size in sizes]



box = [int(i) for i in input("Данные").split()]


def bsort(box):
     quantity = len(box)
     for i in range(quantity):
          for j in range(quantity-i-1):
               if box[j] > box[j+1]:
                    box[j], box[j+1] = box[j+1], box[j]


print(bsort(box))



#box = [3, 0, 7, 8, 12, 23, 5]
print(sorted(box))

print(sorted("78234"))

slides = ["2", 7, 3, "123", "17", True]
print(sorted([int(slide) for slide in slides]))

cities = ["London", "Madrid", "Dubai", "Los Angeles", "New York"]
print(sorted(cities, key=len, reverse=True))




names_with_case = ['harry', 'Suzy', 'al', 'Mark']
print([(ord(name[0]), name[0]) for name in sorted(names_with_case)])

superheroes = ['Spider-Man', 'Batman', 'Aquaman',
               'Superman', 'Iron Man']


def vowels(character):
  return character[0].upper() in 'AEIOU'


print(list(filter(vowels, superheroes)))



import tkinter as tk
import sys

window = tk.Tk()
window.grid_columnconfigure(0, weight=1)
window.title("Lambda")
window.geometry("300x100")
label = tk.Label(window, text="Lambda Calculus")
label.grid(column=0, row=0)
button = tk.Button(
    window,
    text = "REVERSE",
    command=lambda: label.configure(text=label.cget("text")[::-1]),
)
button.grid(column=0, row=1)
window.mainloop()





print((lambda x: x * x)(3))
print((lambda a, b, c=4: a + b + c)(2, b=3))
print((lambda x: [x, x ** 2, x ** 3])(3))

box = ['apple', 'and', 'a', 'donut']
print(list(filter(lambda a: len(a) > 4, box)))


def f(a, b, c):
    return a + b + c

# ЗАДАЧА ПЕРВЫЙ СПОСОБ
print(list(map(f, [1, 2, 3], [10, 20, 30], [100, 200, 300])))  # [111, 222, 333]

# ЗАДАЧА ВТОРОЙ СПОСОБ
list(
    map(
        (lambda a, b, c: a + b + c),
        [1, 2, 3],
        [10, 20, 30],
        [100, 200, 300]
    )
)


list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333]))

animals = ["ferret", "vole", "dog", "gecko"]
sorted(animals, key=len, reverse=True)
sorted(animals, key=lambda s: -len(s))
list(map(lambda n: n * 2, [1, 2, 3, 4, 5]))



def valid(number):
    if not isinstance(number, int):
        raise TypeError("Ошибка. Введите целое число")

    if number < 0:
        raise ValueError("Ошибка. Число должно быть 0 или положильное")

    return "Okay"


print(valid(-23))



superheroes = ['Spider-Man', 'Batman', 'Aquaman',
               'Superman', 'Iron Man']


def vowels(character):
  return character[0].upper() in 'AEIOU'


print(list(filter(vowels, superheroes)))  # TASK 1

print(list(filter(lambda character: character[0].upper() in 'AEIOU', superheroes)))  # TASK 2



def setup_value():
    m = 123

    def new_value():
        nonlocal m
        m = 982

    new_value()
    print(m)


setup_value()



a = 23


def setup_value():
    global a
    a = 52


setup_value()
print(globals())



def some_action(a, b):
    box = "Hello, World!"
    print(locals())


print(some_action(2, 3))



x1, y1 = int(input("X1: ")), int(input("Y1: "))
x2, y2 = int(input("X2: ")), int(input("Y2: "))


if (abs(x1 - x2) <= 1) and (abs(y1 - y2) <= 1):
    print('Да, сможет')
else:
    print('Нет, не сможет')







num = int(input("Введите число для проверки --> "))
order = len(str(num))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print(num, "является Armstrong number")

else:
    print(num, "не является Armstrong number")





def palindrome_checker(word):
    reverse_word = ''.join(word[::-1])
    return word.lower() == reverse_word.lower()


collection_words = ["Level", "New",
                    "Noon", "Jump", "Radar"]

print(list(filter(palindrome_checker,
                  collection_words)))

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

# ЗАДАЧА 1 - СЕНДВИЧ
sandwich_order = input("Which the sandwich do you prefer? ")
if sandwich_order == "Ham Roll":
    print("Price: $1.75")
elif sandwich_order == "Cheese Roll":
    print("Price: $1.80")
elif sandwich_order == "Bacon Roll":
    print("Price: $2.10")
else:
    print("Price: $2.00")

# ЗАДАЧА 2 - УЗОР
import turtle

t = turtle.Pen()
t.shape("turtle")
t.speed(200)
t.color("red")

for x in range(1000):
    t.forward(x)
    t.left(100)

# ЗАДАЧА 3 - ЗВЕЗДА
turtle.bgcolor("blue3")
turtle.fillcolor("yellow")
turtle.bgcolor("blue3")
turtle.begin_fill()
angle = 120

for side in range(5):
    turtle.forward(152)
    turtle.right(angle)
    turtle.forward(152)
    turtle.right(72 - angle)
turtle.end_fill()

import turtle

t = turtle.Pen()
t.shape("turtle")
t.speed(200)
t.color("orange")

for x in range(1000):
    t.forward(x)
    t.left(92)
