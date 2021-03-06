# 피보나치 수열 재귀 함수 활용
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)
# 2 ** N 의 시간 복잡도를 가짐 -> 비효율적임

# 메모이제이션 (한 번 계산한 결과를 메모리 공간에 메모하는 기법) -> 캐싱
# 탑다운 다이나믹 프로그래밍 소스 코드

# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

def fiboM(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fiboM(x - 1) + fiboM(x - 2)
    return d[x]

print(fibo(6))

# 보텀업 다이나믹 프로그래밍 소스 코드

# 앞서 계산될 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현 (보텀업 다이나믹 프로그래밍)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])