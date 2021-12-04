# https://adventofcode.com/2021/day/3#part2

def bin_to_dec(lst):
    # converts binary to decimal form list input
    ans = 0
    n = len(lst[0])
    for i in range(n):
        ans += (2 ** (n-1)) * int(lst[0][i])
        n -= 1
    return ans

def fix(lst, c):
    i = 0
    tmp = lst
    t = len(lst)
    while t > 1:
        # counting the most abundant group
        ans = 0
        for j in tmp:
            if j[i] == '1':
                ans += 1
            else:
                ans -= 1
        if c == 'o':
            ans = 1 if ans >= 0 else 0
        else:
            ans = 0 if ans >= 0 else 1

        print(f"{tmp=}, {ans=}")
        # removing elements from list according
        # to the most abundant group
        s = []
        for j in range(t):
            if int(tmp[j][i]) == ans:
                s.append(tmp[j])
        i += 1
        tmp = s
        t = len(tmp)

    print(f"{tmp=}")
    return tmp

def solve(lst):
    n = len(lst[0])

    orate = bin_to_dec(fix(lst, 'o'))
    crate = bin_to_dec(fix(lst, 'c'))

    print(orate, crate)

    return orate * crate

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        txt = file.read()
        lst = [line for line in txt.splitlines()]
        print(solve(lst))
