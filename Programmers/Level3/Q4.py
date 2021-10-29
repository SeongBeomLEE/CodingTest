# 정수 삼각형
def solution(triangle):
    dp = [[0 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    rows = len(triangle)
    for row in range(1, rows):
        cols = len(triangle[row])
        for col in range(cols):
            if col == 0:
                dp[row][col] = triangle[row][col] + dp[row - 1][col]
            elif col == cols - 1:
                dp[row][col] = triangle[row][col] + dp[row - 1][col - 1]
            else:
                dp[row][col] = max(triangle[row][col] + dp[row - 1][col - 1], triangle[row][col] + dp[row - 1][col])
    answer = max(dp[rows - 1])
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))