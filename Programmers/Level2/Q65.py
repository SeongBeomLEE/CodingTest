# N개의 최소공배수
def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def solution(arr):
    arr.sort()
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
    return answer

arr = [2,6,8,14]

print(solution(arr))