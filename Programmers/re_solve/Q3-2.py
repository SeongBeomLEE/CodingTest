import heapq
def solution(jobs):
    cnt = 0
    start = -1
    now = 0
    answer = 0
    heap = []
    while cnt < len(jobs):
        for job in jobs:
            start_point, end_point = job
            if start < start_point <= now:
                heapq.heappush(heap, (end_point, start_point))
        if heap:
            end_point, start_point = heapq.heappop(heap)
            start = now
            now += end_point
            answer += now - start_point
            cnt += 1
        else:
            now += 1
    return int(answer / len(jobs))