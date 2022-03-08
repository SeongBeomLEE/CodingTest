# 수 정렬하기 3
# 효율적이 메모리 사용을 위하여
# dp의 index를 변수로 val을 cnt로 사용한다.
import sys
dp = [0] * 10001
N = int(input())
for _ in range(N):
    dp[int(sys.stdin.readline())] += 1

for i in range(len(dp)):
    if dp[i] != 0:
        for _ in range(dp[i]):
            print(i)
