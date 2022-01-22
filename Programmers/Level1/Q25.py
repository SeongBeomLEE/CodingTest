# 신고 결과 받기
def solution(id_list, report, k):
    answer = []
    report = set(report)
    user_ben_cnt_dict = {}
    user_ben_li_dict = {}

    for user_id in id_list:
        user_ben_cnt_dict[user_id] = 0
        user_ben_li_dict[user_id] = []

    for r in report:
        user_id, ben_user_id = r.split()
        user_ben_cnt_dict[ben_user_id] += 1
        user_ben_li_dict[user_id] += [ben_user_id]

    ben_user_id_li = []
    for user_id in id_list:
        if user_ben_cnt_dict[user_id] >= k:
            ben_user_id_li.append(user_id)

    for user_id in id_list:
        cnt = 0
        for ben_user_id in ben_user_id_li:
            if ben_user_id in user_ben_li_dict[user_id]:
                cnt += 1

        answer.append(cnt)

    return answer
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))