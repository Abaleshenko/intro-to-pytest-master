# сет данных ячейка нахождения фигуры
x1, y1 = int(input("♞ x ")), int(input("♞ y "))
# куда выполняет ход
x2, y2 = int(input("♞ x ")), int(input("♞ y "))

# delta - разница координат
dx, dy = abs(x1-x2), abs(y1-y2)

if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("Шахматная фигру ♞ сделает свой ход")
else:
    print("Шахматная фигру ♞ не сделает свой ход")



