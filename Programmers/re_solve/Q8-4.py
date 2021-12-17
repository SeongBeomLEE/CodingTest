'''
항상 "ICN" 공항에서 출발

방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수

만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return <- 미리 정렬한다.

tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미

DFS/BFS로 각 공항이 출발해서 갈 수 있는 모든 경로를 탐색하는 것이 맞는 방법임

dict를 deepcopy 해서 사용하는 방법이 맞는 듯 하나 너무 비효율적이다고 생각됨

'''
import copy
from collections import deque
def solution(tickets):
    tickets_dict = {}
    for ticket in tickets:
        a, b = ticket
        if a not in tickets_dict:
            tickets_dict[a] = [b]
        else:
            tickets_dict[a] += [b]

    for key in tickets_dict.keys():
        tickets_dict[key].sort()

    # answer_li = []
    q = deque([[['ICN'], tickets_dict]])
    while q:
        answer, tickets_dict = q.popleft()

        if not tickets_dict:
            # answer_li.append(answer)
            # continue

            break

        a = answer[-1]
        if a not in tickets_dict:
            continue

        for b in tickets_dict[a]:
            _tickets_dict = copy.deepcopy(tickets_dict)
            _answer = answer[:] + [b]
            _tickets_dict[a].remove(b)
            if len(_tickets_dict[a]) < 1:
                del _tickets_dict[a]
            q.append([_answer, _tickets_dict])

    # return sorted(answer_li)[0]

    return answer