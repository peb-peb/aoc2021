# https://adventofcode.com/2021/day/1

def solve(lst):
    cnt = 0
    for i in range(1, len(lst)):
        if lst[i - 1] < lst[i]:
            cnt += 1
    return cnt

if __name__ == "__main__":
    with open('input01.txt', 'r') as file:
        txt = file.read()
        lst = list(map(int, txt.split()))
        print(solve(lst))
