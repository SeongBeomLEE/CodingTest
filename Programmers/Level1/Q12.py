# 모의고사
def solution(answers):
    answer = [0, 0, 0]
    s1_li = [1, 2, 3, 4, 5] * 2001
    s2_li = [2, 1, 2, 3, 2, 4, 2, 5] * 1251
    s3_li = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1001
    for idx in range(len(answers)):
        if answers[idx] == s1_li[idx]: answer[0] += 1
        if answers[idx] == s2_li[idx]: answer[1] += 1
        if answers[idx] == s3_li[idx]: answer[2] += 1
    ret = []
    for idx in range(len(answer)):
        if answer[idx] == max(answer):
            ret.append(idx + 1)
    return ret

answers = [1,2,3,4,5]
# answers = [1,3,2,4,2]
print(solution(answers))