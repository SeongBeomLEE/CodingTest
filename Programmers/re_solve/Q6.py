# 입국심사
def solution(n, times):
    answer = 0
    times.sort()
    left = 0
    right = times[-1] * n
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
        if cnt >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
n = 6
times = [1, 2, 3, 4, 5, 6]
print(solution(n, times))