# 리모컨
N = int(input())
broken_btn = input().split() if 1 <= int(input()) else []
answer = abs(100 - N)

# 모든 숫자 탐색 (완전 탐색)
for num in range(1000001):
    for n in str(num):
        # 해당 숫자 안에 고장난 숫자가 있다면 당연히 만들 수 없는 숫자이므로 사용 X
        if n in broken_btn:
            break
    else:
        answer = min(answer, abs(N - num) + len(str(num)))

print(answer)