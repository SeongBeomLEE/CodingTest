# 튜플
def solution(s):
    s = eval('[' + s[1:-1] + ']')
    s = sorted(s, key = lambda x: len(x))
    answer = []
    for i in s:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
# s = "{{20,111},{111}}"
s = "{{123}}"
print(solution(s))
