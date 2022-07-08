# https://www.acmicpc.net/problem/2577
# 숫자의 개수

def solution(num : int):
    answer = [0] * 10
    for n in str(num):
        answer[int(n)] += 1
    return answer

num = 1

for _ in range(3):
    num *= int(input())

answer = solution(num)
for a in answer:
    print(a)