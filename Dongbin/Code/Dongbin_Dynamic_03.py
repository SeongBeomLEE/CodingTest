# 개미 전사
# 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.
N = int(input())

# 식량정보가 저장된 리스트
array = list(map(int, input().split()))

# 계산된 결과를 저장히가 위한 테이블
dp = [0] * 100

# 다이나믹 프로그래밍 진행 (보텀업)
dp[0] = array[0]
dp[1] = max(array[0], array[1])

for i in range(2, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i])

print(dp[N - 1])

