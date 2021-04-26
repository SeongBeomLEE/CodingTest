# 운영체제 학점 잘 받음?
N = int(input())
array = list(map(int, input().split()))
array.sort()
d = [0] * N
d[0] = array[0]
for i in range(1, N):
    d[i] = d[i - 1] + array[i]
print(sum(d))