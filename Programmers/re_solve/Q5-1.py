def solution(answers):
    cnt_answer = [0, 0, 0]
    answer_1 = [1, 2, 3, 4, 5] * 2001
    answer_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1300
    answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1001
    for idx in range(len(answers)):
        if answer_1[idx] == answers[idx]: cnt_answer[0] += 1
        if answer_2[idx] == answers[idx]: cnt_answer[1] += 1
        if answer_3[idx] == answers[idx]: cnt_answer[2] += 1
    max_val = max(cnt_answer)
    answer = []
    for idx, val in enumerate(cnt_answer):
        if val == max_val: answer.append(idx + 1)
    return sorted(answer)