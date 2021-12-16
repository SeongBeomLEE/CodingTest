import heapq


def solution(operations):
    max_heap = []
    min_heap = []
    for operation in operations:
        action, num = operation.split(' ')
        if action == 'I':
            heapq.heappush(max_heap, -int(num))
            heapq.heappush(min_heap, int(num))
        if max_heap and min_heap:
            if action == 'D':
                if num == '-1':
                    num = heapq.heappop(min_heap)
                    if len(max_heap) == len(min_heap) and -max_heap[0] == num:
                        max_heap = []
                        min_heap = []

                if num == '1':
                    num = heapq.heappop(max_heap)
                    if len(max_heap) == len(min_heap) and -num == min_heap[0]:
                        max_heap = []
                        min_heap = []

                if not max_heap or not min_heap:
                    max_heap = []
                    min_heap = []

        # print(action, num, max_heap, min_heap)
    if not max_heap or not min_heap:
        answer = [0, 0]
    else:
        answer = [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    return answer