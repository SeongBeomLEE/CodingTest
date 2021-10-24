# 단어 뒤집기 2
from sys import stdin
strings = stdin.readline().strip()

stack = []
S = ''
temp = True
for s in strings:
    if s == '<' and temp:
        if S != '': stack.append(S)
        S = ''
        temp = False
    S += s
    if s == '>' and not temp:
        stack.append(S)
        S = ''
        temp = True

if S != '': stack.append(S)

answer = []
for s in stack:
    if s[0] == '<': answer.append(s)
    else:
        s_li = []
        s = s.split(' ')
        for _s in s:
            s_li.append(_s[::-1])
        answer.append(' '.join(s_li))

print(''.join(answer))