# 문자열 분석
import sys
import string
a = list(string.ascii_lowercase)
A = list(string.ascii_uppercase)
num = list(string.digits)

while True:
    answer = [0, 0, 0, 0] # 소문자, 대문자, 숫자, 공백
    strings = sys.stdin.readline().rstrip('\n')

    if not strings:
        break

    for s in strings:
        if s in a: answer[0] += 1
        elif s in A: answer[1] += 1
        elif s in num: answer[2] += 1
        else: answer[3] += 1

    print(' '.join(list(map(str, answer))))