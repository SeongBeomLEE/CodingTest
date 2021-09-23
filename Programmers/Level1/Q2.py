# 신규아이디 추천
import re

# 내 풀이
def solution(new_id):
    answer = new_id
    # 1단계 소문자 변환
    answer = answer.lower()

    # 2단계 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    answer = re.sub('[^0-9a-z._-]','',answer)

    # 3단계 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    answer = re.sub('[.]+', '.', answer)

    # 4단계 마침표(.)가 처음이나 끝에 위치한다면 제거
    if answer[0] == '.':
        answer = answer[1:]

    if answer != '':
        if answer[-1] == '.':
            answer = answer[:-1]

    # 5단계 빈 문자열이라면, new_id에 "a"를 대입
    if answer == '':
        answer = 'a'

    # 6단계 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다
    if len(answer) <= 2:
        add_last = answer[-1]
        while len(answer) <= 2:
            answer += add_last

    return answer

# 깔끔한 풀이
def solution(new_id):
    answer = new_id
    # 소문자 변환
    answer = answer.lower()
    # 소문자, 숫자, -, _, . 제외하고 다 제거
    answer = re.sub('[^a-z0-9\-_.]', '', answer)
    # .이 1개 이상 반복되면 .으로 치환
    answer = re.sub('\.+', '.', answer)
    # 시작 위치와 종료 위치에 . 이 있으면 제거
    answer = re.sub('^[.]|[.]$', '', answer)
    # 공백 문자라면 a로 아니라면 15개 길이 까지 문자로 변환
    answer = 'a' if len(answer) == 0 else answer[:15]
    # 시작 위치와 종료 위치에 . 이 있으면 제거
    answer = re.sub('^[.]|[.]$', '', answer)
    # 길이가 3이상이라면 반환 아니라면 마지막 문자를 문자 길이가 3이 될 때 까지 끝에 더함
    answer = answer if len(answer) > 2 else answer + ''.join([answer[-1] for _ in range(3 - len(answer))])

    return answer

new_id =	"...!@BaT#*..y.abcdefghijklm"
# new_id =	"z-+.^."
# new_id =	"=.="
# new_id =	"123_.def"
# new_id = 	"abcdefghijklmn.p"
print(solution(new_id))