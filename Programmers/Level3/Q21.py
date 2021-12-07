# 불량 사용자
from itertools import product
def solution(user_id, banned_id):
    _ban_id_li = []
    for ban_id in banned_id:
        ban_id_len = len(ban_id)
        ban_id_li = []
        for u_id in user_id:
            if ban_id_len == len(u_id):
                for idx in range(len(ban_id)):
                    if ban_id[idx] != '*' and ban_id[idx] != u_id[idx]: break
                else: ban_id_li.append(u_id)
        _ban_id_li.append(ban_id_li)
    _ban_id_li = list(product(*_ban_id_li))
    answer = []
    for _ban_id in _ban_id_li:
        if len(set(_ban_id)) == len(banned_id):
            answer.append(tuple(sorted(list(_ban_id))))
    return len(set(answer))

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))