# 오픈채팅방
def solution(record):
    answer = []
    user = {}
    for r in record:
        _r = r.split()
        if _r[0] == 'Enter':
            user[_r[1]] = _r[2]
            answer.append([_r[1], "님이 들어왔습니다."])
        elif _r[0] == 'Change':
            user[_r[1]] = _r[2]
        else: answer.append([_r[1], "님이 나갔습니다."])
    return [user[i[0]] + i[1] for i in answer]
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))