# https://adventofcode.com/2021/day/10

# for part 1
SCORE1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

# for part 2
SCORE2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

FORWARD = {'(': ')', '{': '}', '[': ']', '<': '>'}
REVERSE = {r: f for f, r in FORWARD.items()}

def solve1(chunks):
    res = 0
    for chunk in chunks:
        stack = []
        for c in chunk:
            if c in FORWARD:
                stack.append(c)
            else: # c in REVERSE
                if REVERSE[c] == stack[-1]:
                    stack.pop()
                else:
                    res += SCORE1[c]
                    break
    return res

def solve2(chunks):
    res = []
    for chunk in chunks:
        stack = []
        corrupted = False
        for c in chunk:
            if c in FORWARD:
                stack.append(c)
            else: # c in REVERSE
                if REVERSE[c] == stack[-1]:
                    stack.pop()
                else:
                    corrupted = True
        if not corrupted:
            ans = 0
            for bracket in stack[::-1]:
                ans = (ans * 5) + SCORE2[bracket]
            res.append(ans)
    res.sort()
    return res[len(res)//2]

if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        txt = file.read()
        chunks = txt.splitlines()
        print(f"part1: {solve1(chunks)}")
        print(f"part2: {solve2(chunks)}")
