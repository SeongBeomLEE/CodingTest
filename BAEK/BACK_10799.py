# 쇠막대기
bar = list(input())
ans = 0
stack = []

for idx in range(len(bar)):
    if bar[idx] == '(':
        stack.append('(')
    else:
        if bar[idx - 1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1

print(ans)

bar = list(input())
stack = []
answer = 0
for idx in range(len(bar)):
    if bar[idx] == '(':
        stack.append('(')
    else:
        # 레이저 발사
        if bar[idx - 1] == '(':
            stack.pop()
            answer += len(stack)
        # 막대 종료
        else:
            stack.pop()
            answer += 1

print(answer)
