# 접미사 배열
answer = []
S = input()
for i in range(len(S)):
    answer.append(S[i:])
for s in sorted(answer):
    print(s)