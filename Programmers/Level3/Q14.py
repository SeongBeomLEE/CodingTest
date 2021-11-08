# 입국김사
def solution(n, times):
    times.sort()
    answer = -1
    left = 0
    right = times[-1] * n
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
        if cnt >= n :
            if answer < 0 : answer = mid
            else: answer = min(answer, mid)
            right = mid - 1
        elif cnt < n : left = mid + 1
    return answer

n = 6
times = [7, 10]
print(solution(n, times))