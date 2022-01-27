# 2 x n 타일링
'''
0 = 1
1 = 2
2 = 3
3 = 5
'''

def solution(n):
    dp = [0] * (n)
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1000000007
    answer = (dp[n - 1]) % 1000000007
    return answer

n = 4
print(solution(n))