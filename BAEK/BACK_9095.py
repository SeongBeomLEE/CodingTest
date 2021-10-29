# 1, 2, 3 더하기
# d[n] = d[n-3] + d[n-2] + d[n-1]  n >= 4
n = 11
d = [0] * (n + 1)
d[0] = 0
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, n + 1):
    d[i] = d[i - 3] + d[i - 2] + d[i - 1]

for _ in range(int(input())):
    print(d[int(input())])