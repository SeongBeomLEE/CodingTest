# 더 맵게
import heapq
def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville:
        h = heapq.heappop(scoville)
        if h >= K:
            break
        if not scoville and h < K:
            answer = -1
            break
        t = heapq.heappop(scoville)
        sco = h + (t * 2)
        heapq.heappush(scoville, sco)
        answer += 1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))