'''
dp는 각 N 사용 횟수의 결과를 저장
'''
def solution(N, number):
    dp = [[] for _ in range(9)]
    answer = -1
    for i in range(1, 9):
        for j in range(1, i + 1):
            for c in dp[i - j]:
                for k in dp[j]:
                    dp[i].append(c - k)
                    dp[i].append(c + k)
                    dp[i].append(c * k)
                    if k != 0: dp[i].append(int(c / k))
        dp[i].append(int(str(N) * i))
        if number in dp[i]:
            return i

    return answer