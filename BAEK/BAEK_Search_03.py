# 랜선 자르기
N, K = 4, 11
array = [802, 743, 457, 539]

N, K = map(int, input().split())
array = []
for _ in range(N):
    array.append(int(input()))

# start = 0으로 하면 ZeroDivisionError 발생
# 굳이 0부터 시작할 필요가 없기 때문에
start = 1
end = max(array)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in array:
        sum += i // mid
    if sum >= K :
        result = mid
        start = mid + 1
    if sum < K :
        end = mid - 1

print(result)

