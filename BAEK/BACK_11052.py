# 카드 구매하기

# 민규가 살 카드의 개수
n = int(input())
p = list(map(int, input().split()))

d = [0] * (n + 1)
for i in range(1, len(p) + 1):
    for j in range(i, n + 1):
        d[j] = max(d[j - i] + p[i - 1], d[j])

print(d[n])