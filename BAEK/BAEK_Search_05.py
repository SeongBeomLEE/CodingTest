# 공유기 설치
N, M = 5, 3
array = [1, 2, 8, 4, 9]

# N, M = map(int, input().split())
# array = []
# for _ in range(N):
#     array.append(int(input()))

array.sort()

start = 1
end = array[-1] - array[0]

result = 0

while start <= end:
    mid = (start + end) // 2
    old = array[0]
    count = 1

    for i in range(1, N):
        if array[i] >= old + mid :
            count += 1
            old = array[i]

    if count < M : end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
