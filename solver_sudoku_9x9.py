suite = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def render(line):
    for i in range(0, len(line)):
        """После каждых 3-х строк массива suite выполнить подчёркивание"""
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        """len(suite[0]) - определить длину одной Серии(строки) данных"""
        for j in range(len(line[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end=" ")

            """Если край борда, пробел не добавлять, иначе после каждого столбика добавлять пробел"""
            if j == 8:
                print(line[i][j])
            else:
                print(str(line[i][j]), end=" ")


def empty_checker(line):
    for i in range(len(line)):
        for j in range(len(line[0])):
            """Вернуть координаты расположение 0 в таблице"""
            if line[i][j] == 0:
                return i, j
    """Иначе оставить, то число, которые уже стояло в борде"""
    return None  # None - ничего не делать, отсуствие функционалньости и поведения


def decide_sudoku(line):
    """Главная функция"""

    lookout = empty_checker(line)

    if not lookout:
        return True
    else:
        series, col = lookout

    for i in range(1, 10):
        if checking_solver(line, i, (series, col)):
            line[series][col] = i

            if decide_sudoku(line):
                return True

            line[series][col] = 0
    return False


def checking_solver(line, digit, coords):
    # Check row
    for i in range(len(line[0])):
        if line[coords[0]][i] == digit and coords[1] != i:
            return False

    # Check column
    for i in range(len(line)):
        if line[i][coords[1]] == digit and coords[0] != i:
            return False

    # Check box
    box_x = coords[1] // 3
    box_y = coords[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if line[i][j] == digit and (i, j) != coords:
                return False

    return True


render(suite)
decide_sudoku(suite)
print("\n---------------------------SOLVE---------------------------\n")
render(suite)