# 여행결로
import copy
def solution(tickets):
    m = {}
    tickets.sort()
    for ticket in tickets:
        if ticket[0] not in m:
            m[ticket[0]] = [ticket[1]]
        else:
            m[ticket[0]] += [ticket[1]]
    q = [[['ICN'], m]]
    while True:
        ans, m = q.pop(0)
        if not m :
            return ans
        s = ans[-1]
        try:
            for go in m[s]:
                _m = copy.deepcopy(m)
                _m[s].remove(go)
                _ans = list(ans) + [go]
                if not _m[s]:
                    del _m[s]
                q.append([_ans, _m])
        except: continue
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))