# https://adventofcode.com/2021/day/4

def update_board(board, draw):
    for i in range(5):
        for j in range(5):
            if board[i][j] == draw:
                board[i][j] = '-'
    return board

def is_won(board):
    for i in range(5):
        cnt_row, cnt_col = 0, 0
        for j in range(5):
            # for row
            if board[i][j] == '-':
                cnt_row += 1
            if cnt_row == 5:
                return True
            # for column
            if board[j][i] == '-':
                cnt_col += 1
            if cnt_col == 5:
                return True
    return False

def calculate(board, last_draw):
    result = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != '-':
                result += int(board[i][j])
    result *= int(last_draw)
    return result

def solve(num_draw, boards):
    for i in num_draw:
        for j in range(len(boards)):
            boards[j] = update_board(boards[j], i)
            if is_won(boards[j]):
                return calculate(boards[j], i)

if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        txt = file.read()
        lst = [line for line in txt.splitlines()]

        # handling number draw
        num_draw = lst[0].split(',')

        # handling boards
        boards = []
        board = []
        for i in range(len(lst[2:])):
            if lst[2:][i] == '':
                continue
            board.append(lst[2:][i].split())
            if len(board) == 5:
                boards.append(board)
                board = []

        print(solve(num_draw, boards))
