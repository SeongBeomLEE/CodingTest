# 아이디어
# 계속 숫자를 더해가다가 666이 글자에 포함되면
# count 1을 더하고
# count가 n과 동일하게 되면 그 값을 반환
n = int(input())
count = 0
six_n = 666
while True:
    if '666' in str(six_n): count += 1
    if count == n : print(six_n); break
    six_n += 1

