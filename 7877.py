players = '✖●'
squares = [' ']*9

board = '''
 {0} | {1} | {2} 
- - - - - -
 {3} | {4} | {5} 
- - - - - -
 {6} | {7} | {8} 
'''

win_cases = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontals
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # verticals
    (0, 4, 8), (2, 4, 6)              # diagonals
]


def winner_check(player):
    for a, b, c in win_cases:
        if {squares[a], squares[b], squares[c]} == {player}:
            return True


while 1:
    print(board.format(*squares))

    """
    Сначала проверяем, если позиция следующего игрока после последнего ход предыдущего имеет выиграшный кейс, 
    только объёявить о победе
    """

    if winner_check(players[1]):
        print(f'*** \n{players[1]} ПОБЕДИЛ ИГРУ!\n***')
        break

    if ' ' not in squares:
        print('НИЧЬЯ!!')
        break

    move = input(f'{players[0]} to move [0-8] > ')

    if not 0 <= int(move) <= 8 or not move.isdigit() or squares[int(move)] != ' ':
        print('Неправильный ход')
        continue


    """
    Крестик делает ход в борде это поле заполняется крестиком, а потом в players ✖● меняются на ●✖ 
    и теперь ход ● для новой итерации
    """
    squares[int(move)], players = players[0], players[::-1]