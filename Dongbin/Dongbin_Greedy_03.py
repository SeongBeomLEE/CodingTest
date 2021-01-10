# 숫자 카드 게임
# 아이디어
# 모든 행에서 가장 작은 값들을 찾는다
# 그 중에서 가장 큰 값이 우리가 첫번째로 뽑아야 하는 값이다.

N, M = map(int, input().split())
result = 0
for _ in range(N):
    data = list(map(int,input().split()))
    result = max(result, min(data))

print(result)
