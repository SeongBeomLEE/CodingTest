# 멀리 뛰기
'''
1 = 1
2 = 2
3 = 3
4 = 5
5 = 8
11111
1112
122
2111
221

1211
1121
212

'''
def solution(n):
    dp = [0] * 2001
    dp[0] = 1
    dp[1] = 2
    dp[2] = 3
    for i in range(3, 2001):
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp[n - 1] % 1234567