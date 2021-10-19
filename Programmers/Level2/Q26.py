# 괄호 회전하기
def solution(s):
    answer = 0
    s = list(s)
    for idx in range(0, len(s)):
        _s = s[idx:] + s[:idx]
        stack = []

        for char in _s:
            if not stack:
                stack.append(char)
            elif stack[-1] == '[':
                if char == ']': stack.pop()
                else: stack.append(char)
            elif stack[-1] == '(':
                if char == ')': stack.pop()
                else: stack.append(char)
            elif stack[-1] == '{':
                if char == '}': stack.pop()
                else: stack.append(char)

        if not stack: answer += 1

    return answer
s = '[)(]'
# s = "}]()[{"
print(solution(s))
