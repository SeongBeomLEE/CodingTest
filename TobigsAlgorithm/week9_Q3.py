# 투빅 코인
N = int(input())
array = list(map(int, input().split()))

result = 0
cnt = 0
ret = 0

for i in range(0, N - 1):
    if array[i] <= max(array[i+1:]):
        ret += array[i]
        cnt += 1
    else:
        result += array[i] * cnt - ret
        ret = 0
        cnt = 0

# 마지막 순서를 체크하지 못해서 만듬
result += array[N - 1] * cnt - ret

print(result)
