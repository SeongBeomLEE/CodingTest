# 이중우선순위큐
import heapq
def solution(operations):
    answer = []
    for operation in operations:
        o, n = operation.split(' ')
        if o == 'I':
            heapq.heappush(answer, int(n))
        elif o == 'D' and n == '1':
            if answer: answer.remove(max(answer))
        elif o == 'D' and n == '-1':
            if answer: heapq.heappop(answer)
    if answer: return [max(answer), heapq.heappop(answer)]
    else: return [0, 0]

operations = ["I 7","I 5","I -5","D -1"]
print(solution(operations))