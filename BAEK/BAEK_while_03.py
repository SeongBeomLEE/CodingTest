N = int(input()) #입력 받은 수
Check_N = N # while 문에 들어갈 N
count = 0 # 사이클 횟수
while True:
    ten = N // 10 # 10의 자리
    one = N % 10 # 1의 자리
    N = one*10 + ((ten+one)%10) # 결국 문제는 처음 10의 자리와 1의 자리를 더 했을때의 일의 자릿수를 계쏙 더함
    count = count + 1 # 사이클 추가
    if (N == Check_N): # 새로운 N과 처음 N이 같다면 종료
        break
print(count)