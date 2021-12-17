'''
00 = 1

00 = 1
01 = 00
02 = 01
03 = 02

10 = 00
11 = 10 + 01

1 1 1 1
1 0 1 2
1 1 2 4
'''

def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if [col + 1, row + 1] not in puddles:
                if row == 0 and col == 0:
                    dp[row][col] = 1
                elif row == 0:
                    dp[row][col] += dp[row][col - 1]
                elif col == 0:
                    dp[row][col] += dp[row - 1][col]
                else:
                    dp[row][col] += dp[row][col - 1] + dp[row - 1][col]

    answer = dp[-1][-1] % 1000000007
    return answer