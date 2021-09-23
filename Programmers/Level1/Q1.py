# 로또의 최고 순위와 최저 순위

# 내 풀이
def solution(lottos, win_nums):
    zero_cnt = 0
    mat_cnt = 0

    for lotto in lottos:
        if lotto in win_nums :
            mat_cnt += 1
        if lotto == 0 :
            zero_cnt += 1

    if mat_cnt == 0: down_ans = 6
    else: down_ans = 6 - mat_cnt + 1

    total_cnt = mat_cnt + zero_cnt
    if total_cnt == 0: up_ans = 6
    else: up_ans = 6 - total_cnt + 1

    return [up_ans, down_ans]

# 깔끔한 풀이
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0

    for win_num in win_nums:
        if win_num in lottos :
            ans += 1

    return [rank[ans + cnt_0], rank[ans]]


lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
print(solution(lottos, win_nums))