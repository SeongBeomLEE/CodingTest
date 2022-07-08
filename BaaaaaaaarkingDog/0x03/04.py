# https://www.acmicpc.net/problem/3273
# 두 수의 합

def solution(N : int, array : list[int], x : int):
    answer = 0
    dp = [0] * 3000001
    for n in array:
        if (x - n) >= 0:
            if dp[x - n] == 1: # n이 j라고 가정하고 풀이, 미리 dp를 초기화하고 n을 i로 가정하고 풀면 틀림
                answer += 1
        dp[n] = 1
    return answer

n = int(input())
array = list(map(int, input().split()))
x = int(input())

print(solution(n, array, x))