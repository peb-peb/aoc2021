# https://adventofcode.com/2021/day/2

def solve(lst):
    x, y = 0, 0
    for i in lst:
        if i[0] == 'forward':
            x += int(i[1])

        if i[0] == 'down':
            y += int(i[1])
        elif i[0] == 'up':
            y -= int(i[1])
    return x * y

if __name__ == "__main__":
    with open('input01.txt', 'r') as file:
        txt = file.read()
        lst = [line.split() for line in txt.splitlines()]
        print(solve(lst))
