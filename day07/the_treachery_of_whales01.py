# https://adventofcode.com/2021/day/7#part2

def solve(pos):
    n = len(pos)
    res = 1000000000
    for i in range(n):
        summ = 0
        for j in range(n):
            x = abs(i - pos[j])
            summ += (x * (x + 1)) // 2
        if summ < res:
            res = summ
    return res

if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        txt = file.read()
        pos = [int(ele) for ele in txt.split(',')]
        print(solve(pos))
