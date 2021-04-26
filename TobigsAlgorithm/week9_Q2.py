# 라면 물은 생명
N = int(input())
result = 0
while N > 0:
    N -= 3
    result += 1
    if N % 5 == 0:
        result += N // 5
        N = 0

if N == 0:
    print(result)
else:
    print(-1)