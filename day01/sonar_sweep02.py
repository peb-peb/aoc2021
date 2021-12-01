# https://adventofcode.com/2021/day/1#part2

def gen_lst(lst):
    sum_lst = []
    for i in range(2, len(lst)):
        sum_lst.append(lst[i - 2] + lst[i - 1] + lst[i])
    return sum_lst

def solve(lst):
    cnt = 0
    sum_lst = gen_lst(lst)
    for i in range(len(sum_lst)):
        if sum_lst[i - 1] < sum_lst[i]:
            cnt += 1
    return cnt

if __name__ == "__main__":
    with open('input02.txt', 'r') as file:
        txt = file.read()
        lst = list(map(int, txt.split()))
        print(solve(lst))
