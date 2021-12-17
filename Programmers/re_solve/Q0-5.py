# 여행 경로
import copy
def solution(tickets):
    answer = []
    q = [[['ICN'], tickets]]
    while q:
        vis_city, rem_tickets = q.pop(0)

        if not rem_tickets:
            answer.append(vis_city)

        for idx, ticket in enumerate(rem_tickets):
            if vis_city[-1] == ticket[0]:
                _vis_city = vis_city[:]
                _rem_tickets = copy.deepcopy(rem_tickets)
                del _rem_tickets[idx]
                q.append([_vis_city + [ticket[1]], _rem_tickets])

    return sorted(answer)[0]
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))