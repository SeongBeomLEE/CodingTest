# 후위표기식2

N = int(input())
strings = input()
nums = []
for _ in range(N):
    nums.append(int(input()))
stack = []

for s in strings:
    if s not in ['*', '+', '/', '-']:
        stack.append(nums[ord(s) - ord('A')])
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if s == '*': stack.append(num1 * num2)
        elif s == '+': stack.append(num1 + num2)
        elif s == '/': stack.append(num1 / num2)
        elif s == '-': stack.append(num1 - num2)

print(f'{stack[0]:.2f}')