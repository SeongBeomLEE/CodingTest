'''
max_time 은 times의 최댓값 * n

위에 시간을 기준으로 이분탐색을 통해서
최소 시간으로 n명 이상을 심사할 수 있는 시간을 찾는다.

'''
def solution(n, times):
    left = 1
    right = max(times) * n
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
        if cnt >= n:
            if answer == -1:
                answer = mid
            else:
                answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1
    return answer