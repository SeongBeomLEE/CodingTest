# 스택
stack = []
line_li = [input().split(' ') for i in range(int(input()))]
for line in line_li:
    if line[0] == 'push':
        stack.append(line[1])
    if line[0] == 'pop':
        if stack: print(stack.pop())
        else: print(-1)
    if line[0] == 'size': print(len(stack))
    if line[0] == 'empty':
        if stack: print(0)
        else: print(1)
    if line[0] == 'top':
        if stack: print(stack[-1])
        else: print(-1)