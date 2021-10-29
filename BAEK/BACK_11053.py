# 가장 긴 증가하는 부분 수열
N = int(input())
dp = [1] * (N + 1)
arr = list(map(int, input().split()))
for idx in range(0, N):
    for j in range(idx):
        if arr[j] < arr[idx]:
            dp[idx] = max(dp[j] + 1, dp[idx])
print(max(dp))

