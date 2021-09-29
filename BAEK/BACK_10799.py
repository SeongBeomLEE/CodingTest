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
