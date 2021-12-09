# https://adventofcode.com/2021/day/4

def if_horizontal_bing(board,y):
    for elem in board[y]:
        if elem != 'x':
            return False
    return True 


def if_vertical_bingo(board, x):
    for j in range(len(board)):
        if board[j][x] != 'x':
            return False
    return True


def did_the_board_win(board, y, x):
    return if_horizontal_bing(board, y) or if_vertical_bingo(board, x)


def find_winner():
    for random in randoms:
        for b_i in range(len(boards)):
            for r_i in range(len(boards[b_i])):
                for n_i in range(len(boards[b_i][r_i])):
                    if boards[b_i][r_i][n_i] == random:
                        boards[b_i][r_i][n_i] = 'x'
                        if did_the_board_win(boards[b_i],r_i,n_i):
                            return boards[b_i], random


def count_boards_left_numbers(board):
    result = 0
    for row in board:
        for num in row:
            if num != 'x':
                result += num
    return result


def p1():
    winner, last_number = find_winner()
    print("p1 = ", count_boards_left_numbers(winner) * last_number)


def find_loser():
    left = set(range(len(boards)))
    for random in randoms:
        for b_i in range(len(boards)):
            if b_i in left:
                for r_i in range(len(boards[b_i])):
                    for n_i in range(len(boards[b_i][r_i])):
                        if boards[b_i][r_i][n_i] == random:
                            boards[b_i][r_i][n_i] = 'x'
                            if did_the_board_win(boards[b_i],r_i,n_i):
                                if len(left)==1:
                                    return boards[next(iter(left))], random
                                left.discard(b_i)


def p2():
    loser, last_number = find_loser()
    print("p2 = ", count_boards_left_numbers(loser) * last_number)


boards = None
with open('i.txt', 'r') as f:
    randoms = [int(x) for x in f.readline().strip().split(',')] 

    f.readline()
    boards = []
    board = []
    for line in f.readlines():
        if line == '\n':
            boards.append(board)
            board = []
        else:
            row = [int(x) for x in list(filter(lambda y: y!='', line.strip().split(' ')))]
            board.append(row)
p1()
p2()

