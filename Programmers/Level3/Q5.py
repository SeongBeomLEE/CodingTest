# 등굣길
def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    for y in range(n):
        for x in range(m):
            if [x + 1, y + 1] in puddles:
                dp[y][x] = 0
            elif x == 0 and y == 0: continue
            elif y == 0:
                dp[y][x] += dp[y][x - 1]
            elif x == 0:
                dp[y][x] += dp[y - 1][x]
            else:
                dp[y][x] = dp[y - 1][x] + dp[y][x - 1]

    return dp[-1][-1] % 1000000007

m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))