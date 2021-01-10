# 브루트 포스란?
# 모든 경우의 수를 탐색하는 알고리즘
# 문제
# 입력된 N(카드의 개수), M, N개의 카드 중 중
# 모든 N개의 카드 중에 중복을 포함하지 않고 3개를 뽑아서 다 더한 후
# 그 중에서 M 이하의 수 중에 가장 큰 값을 출력

# 아이디어
# 1. 카드를 모두 리스트로 받는다
# 2. 다중 반복문을 사용하여 모든 경우의수를 탐색한다.
# 3. 여기서 중요한 것은 중복은 포함되지 않는다는 것
# 4. 첫번째는 최종 카드의 개수 -2 만큼 반복
# 5. 두번째는 첫번째 카드의 인덱스 +1 ~ 치종 카드의 개수 -1 만큼 반복
# 6. 세번째 반복문은 두번째 카드의 인덱스 +1 부터 최종 카드 까지 반복
# 7. 그 숫자의 합 중에서 M 초과는 제외하고 나머지 값 중 최대값을 출력

N, M = map(int,input().split())
card_list = list(map(int, input().split()))
result = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if card_list[i] + card_list[j] + card_list[k] > M: continue
            result = max(result, card_list[i] + card_list[j] + card_list[k])

print(result)