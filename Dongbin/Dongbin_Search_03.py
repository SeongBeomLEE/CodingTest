# 떡볶이 떡 만들기
# N, M = map(int, input().split())
# array = list(map(int, input().split()))

N, M = 4, 6
array = [19, 15, 10, 17]

start = 0
end = max(array)

'''
while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in array:
        if (i - mid) > 0: sum += i - mid

    if sum == M: break
    elif sum < M : end = mid - 1
    else: start = mid + 1

print(mid)
'''

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in array:
        if (i - mid) > 0: sum += i - mid
    if sum < M : end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)