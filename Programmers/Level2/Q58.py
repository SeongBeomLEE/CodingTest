# 땅따먹기
def solution(land):
    n = len(land)
    dp = [[0, 0, 0, 0] for i in range(n)]
    dp[0] = land[0]
    for i in range(1, n):
        for j in range(4):
            for y in range(4):
                if j != y:
                    dp[i][j] = max(dp[i][j], land[i][j] + dp[i - 1][y])
    return max(dp[-1])

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))