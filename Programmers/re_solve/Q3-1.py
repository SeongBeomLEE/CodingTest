import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        f_min_val = heapq.heappop(scoville)
        if f_min_val < K:
            if not scoville:
                answer = -1
                break
            answer += 1
            s_min_val = heapq.heappop(scoville)
            val = f_min_val + (s_min_val * 2)
            heapq.heappush(scoville, val)
        else: break
    return answer