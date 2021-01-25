# 바닥 공사

N = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, N + 1):
    # 점화식을 생각하자.
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[N])

