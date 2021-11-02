# 디스크 컨트롤러
# https://programmers.co.kr/questions/12430
# 아직 이해를 못함 다시 공부해야함
import heapq
def solution(jobs):
    jobs.sort()
    answer, now, start, idx = 0, 0, -1, 0
    nums = len(jobs)
    heap = []
    while idx < len(jobs):
        for s, d in jobs:
            if start < s <= now:
                heapq.heappush(heap, [d, s])
        if heap:
            d, s = heapq.heappop(heap)
            start = now
            now += d
            answer += (now - s)
            idx += 1
        else:
            now += 1

    return answer // nums

# [작업이 요청되는 시점, 작업의 소요시간]
jobs = [[0, 3], [1, 9], [2, 6]]
jobs = [[0, 3], [0, 2], [1, 9], [2, 6]]
print(solution(jobs))