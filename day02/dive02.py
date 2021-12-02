# https://adventofcode.com/2021/day/2#part2

def solve(lst):
    x, y = 0, 0
    aim = 0
    for i in lst:
        n = int(i[1])
        if i[0] == 'forward':
            x += n
            y += aim * n

        if i[0] == 'down':
            aim += n
        elif i[0] == 'up':
            aim -= n
    return x * y

if __name__ == "__main__":
    with open('input01.txt', 'r') as file:
        txt = file.read()
        lst = [line.split() for line in txt.splitlines()]
        print(solve(lst))
