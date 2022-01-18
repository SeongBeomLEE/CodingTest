# 신규어이디 추천
import re
def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)

    # 3단계
    new_id = re.sub('\.+', '.', new_id)

    # 4단계
    for _ in range(2):
        match_val = re.match('\.+', new_id)
        if match_val:
            match_idx = match_val.span()[-1]
            new_id = new_id[match_idx:]
        new_id = new_id[::-1]

    # 5단계
    if new_id == '':
        new_id += 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]

        new_id = new_id[::-1]
        match_val = re.match('\.+', new_id)
        if match_val:
            match_idx = match_val.span()[-1]
            new_id = new_id[match_idx:]
        new_id = new_id[::-1]

    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]

    answer = new_id
    return answer

new_id = '...!@BaT#*..y.abcdefghijklm'
print(solution(new_id))