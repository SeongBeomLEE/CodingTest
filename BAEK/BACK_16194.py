# 카드 구매하기 2
n = int(input())
p = list(map(int, input().split()))
d = [100001] * (n + 1)
d[0] = 0
for i in range(1, len(p) + 1):
    for j in range(i, n + 1):
        d[j] = min(d[j - i] + p[i - 1], d[j])

print(d[n])