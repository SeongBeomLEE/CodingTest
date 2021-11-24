# 삼각 달팽이
def solution(n):
    total = sum([i for i in range(1, n + 1)])
    turn_li = [n]
    for i in range(n - 1, 0, -1):
        turn_li.append(turn_li[-1] + i)
    ans = [[0] * i for i in range(1, n + 1)]

    row = 0
    col = 0
    for i in range(1, total + 1):
        ans[row][col] = i
        for idx in range(len(turn_li)):
            if i < turn_li[idx]: break
        mod = idx % 3
        if mod == 0: row += 1
        if mod == 1: col += 1
        if mod == 2:
            row -= 1
            col -= 1
    answer = []
    for i in ans:
        answer += i
    return answer

n = 5
print(solution(n))