# 알록달록 울타리
n, k = map(int, input().split())
array = []

for _ in range(n):
    array.append(int(input()))

d = [0] * (k + 1)
for i in range(n):
    for j in range(array[i], k + 1):
        # 모든 경우의 수를 구함
        d[j] = d[j] + d[j - array[i]] + 1

# 겹치는 것을 빼주기 위해서
print(d[-1] - d[-2])





