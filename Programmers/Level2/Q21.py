# 순위 검색
def solution(info, query):
    info = [i.split(" ")for i in info]
    query = [[j for j in i.split(" ") if j != 'and'] for i in query]
    result = {}
    answer = []

    for i in info:
        for f in ['-'] + [i[0]]:
            for s in ['-'] + [i[1]]:
                for t in ['-'] + [i[2]]:
                    for q in ['-'] + [i[3]]:
                        if f+s+t+q not in result:
                            result[f + s + t + q] = [int(i[4])]
                        else:
                            result[f + s + t + q] += [int(i[4])]

    for key in result.keys():
        result[key].sort()

    for q in query:
        cnt = 0
        if q[0] + q[1] + q[2] + q[3] in result:
            li = result[q[0] + q[1] + q[2] + q[3]]
            right = len(li) - 1
            left = 0
            while left <= right :
                mid = (left + right) // 2
                if li[mid] < int(q[4]):
                    left = mid + 1
                elif li[mid] >= int(q[4]):
                    right = mid - 1
            cnt = len(li) - left
        answer.append(cnt)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))