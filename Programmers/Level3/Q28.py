# 징검다리 건너기
# 이진탐색으로 구하자
def solution(stones, k):
    answer = 0
    left = 0
    right = max(stones)
    while left <= right:
        tmp = False
        mid = (left + right) // 2
        cnt = 0
        for idx in range(len(stones)):
            if stones[idx] < mid:
                cnt += 1
            else:
                cnt = 0

            if cnt >= k:
                tmp = True
                break
        else:
            answer = max(answer, mid)
            left = mid + 1
        if tmp:
            right = mid - 1
    return answer