# 카잉 달려
T = int(input())
answer = []
for _ in range(T):
    M, N, x, y = map(int, input().split())
    while x <= M * N:
        if (x - y) % N == 0:
            k = x
            break
        x += M
    else:
        k = -1
    print(k)
