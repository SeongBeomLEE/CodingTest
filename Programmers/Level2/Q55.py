# 올바른 괄호
def solution(ss):
    answer = True
    stack = []
    for s in ss:
        if not stack:
            stack.append(s)
        else:
            if stack[-1] == '(' and s == ')':
                stack.pop()
            else: stack.append(s)
    if stack:
        answer = False
    return answer
s = ")()("
print(solution(s))