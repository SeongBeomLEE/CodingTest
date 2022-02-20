# 공유기 설치
N, C = map(int, input().split())
array = []
for _ in range(N):
    array.append(int(input()))

array.sort()

start = array[0]
end = array[-1] - array[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    current = array[0]
    count = 1

    for i in range(1, N):
        if array[i] >= current + mid :
            count += 1
            current = array[i]

    # print(mid, start, end, count)

    if count >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
