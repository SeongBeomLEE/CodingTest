# 개선된 다익스트라 알고리즘
# 우선순위 큐 자료구조 사용
# 우선순위가 가종 높은 데이터를 가장 먼저 삭제하는 자료구조
import heapq

# 오름차순 힙 정렬
def heapsort_up(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

# 내림차순 힙 정렬
def heapsort_down(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result