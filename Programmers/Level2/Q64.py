# JadenCase 문자열 만들기
def solution(s):
    s_li = s.split(' ')
    new_s_li = []
    for s in s_li:
        s = list(s)
        for idx, val in enumerate(s):
            if idx == 0: s[idx] = val.upper()
            else: s[idx] = val.lower()
        new_s_li.append(s)
    answer = ''
    for s in new_s_li:
        answer += ' ' + ''.join(s)
    return answer[1:]
s = "3people unFollowed ME"
print(solution(s))