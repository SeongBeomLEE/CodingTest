# 스택 수열
def solve(nums):
    answer = []
    stack = []
    cnt = 1
    for num in nums:
        while cnt <= num:
            stack.append(cnt)
            answer.append('+')
            cnt += 1

        if stack[-1] == num:
            stack.pop()
            answer.append('-')
        else:
            return ['NO']

    return answer

nums = []
for _ in range(int(input())):
    nums.append(int(input()))

for answer in solve(nums):
    print(answer)