# https://adventofcode.com/2021/day/3

def bin_to_dec(lst):
    # converts binary to decimal form list input
    ans = 0
    n = len(lst)
    for i in range(n):
        ans += (2 ** (n-1)) * lst[i]
        n -= 1
    return ans

def solve(lst):
    n = len(lst[0])
    ans = [0] * n
    for i in range(n):
        for j in lst:
            if j[i] == '1':
                ans[i] += 1
            else:
                ans[i] -= 1

    gamma = [1 if i > 1 else 0 for i in ans]
    epsilon = [0 if i > 1 else 1 for i in ans]

    grate = bin_to_dec(gamma)
    erate = bin_to_dec(epsilon)

    # print(ans, grate, erate)

    return grate * erate

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        txt = file.read()
        lst = [line for line in txt.splitlines()]
        print(solve(lst))
