# 와인 컨퍼는 즐거워
# 백준 계단 오르기와 동일한 점화식을 활용

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
d = [0] * 100001
d[0] = array[0]
d[1] = array[0] + array[1]
d[2] = max(array[1] + array[2], array[0] + array[2])
for i in range(3, n):
    d[i] = max(d[i - 3] + array[i - 1] + array[i], d[i - 2] + array[i])

print(max(d))
