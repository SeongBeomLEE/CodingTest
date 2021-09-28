# 제로
stack = []
for _ in range(int(input())):
    N = int(input())
    if N != 0 : stack.append(N)
    else: stack.pop()
if stack: print(sum(stack))
else: print(0)