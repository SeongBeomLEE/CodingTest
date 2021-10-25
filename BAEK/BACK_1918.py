# 후위 표기식2 - 진행중

strings = '(A+(B*C))-(D/E)'

stack = []
S = ''
for s in strings:
    print(s, stack)
    if s not in ['*', '+', '/', '-', '(', ')']:
        S += s
    else:
        if stack:
            if s == ')':
                while stack[-1] != '(':
                    S += stack.pop()
                stack.pop()
            else:
                if s == '(': stack.append(s)
                else:
                    if stack[-1] in ['+', '-'] and s in ['+', '-']:
                        S += stack.pop()
                        stack.append(s)
                    elif stack[-1] in ['+', '-'] and s in ['*', '/']:
                        stack.append(s)
                    elif stack[-1] in ['*', '/'] and s in ['*', '/']:
                        S += stack.pop()
                        stack.append(s)
                    elif stack[-1] in ['*', '/'] and s in ['+', '-']:
                        stack.append(s)
        else: stack.append(s)

print(S + ''.join(list(reversed(stack))))