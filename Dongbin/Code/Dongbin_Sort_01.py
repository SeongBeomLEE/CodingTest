# 선택 정렬
def selectionSort(array):
    for i in range(len(array)):
        min_idx = i # 가장 작은 원소의 인덱스
        # 처음 선택을 제외한 나머지 모든 원소를 탐색
        for j in range(i+1, len(array)):
            # 처음 선택된 값보다 작은 값이 나오면 그 값을 가장 작은 값의 인덱스로 선택
            if array[min_idx] > array[j]:
                min_idx = j
        # 가장 작은 원소를 찾으면 이제 그 값과 스와프
        array[i], array[min_idx] = array[min_idx], array[i]

    return array

# 삽입 정렬
def insertionSort(array):
    # 왼쪽으로 값을 삽입할 것이기 때문에 두번째 원소 부터 시작
    for i in range(1, len(array)):
        # 왼쪽으로 값을 탐색
        for j in range(i, 0, -1):
            # 만약 처음 값보다 왼쪽 값이 크다면 두 개의 값을 스와프
            # 왜? array[j]가 array[j-1]의 오른쪽에 존재하는 값이기 때문에
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            # 만약 찾은 값 중에 작은 값을 만나면 반복을 멈춤
            else: break

    return array

# 퀵 정렬
def quickSort(array):
    # 반씩 나눠서 정렬을 하는 알고리즘
    # 재귀함수를 활용하기 떼문에 재귀 함수의 종료조건을 명시
    # 원소가 1개만 남는다면 종료
    if len(array) <= 1:
        return array

    # 첫번째 원소가 기준
    pivot = array[0]
    # 첫번째 원소를 제외한 모든 원소가 정렬될 원소
    tail = array[1:]

    # 기준인 pivot 보다 작다면 왼쪽으로 정렬
    left_side = [x for x in tail if x <= pivot]
    # 크다면 오른쪽으로 정렬
    right_side = [x for x in tail if x > pivot]

    # 피봇을 기준으로 왼쪽 배열과 오른쪽 배열을 나눔
    # 계속 반복하여 배열을 정렬해나감
    return quickSort(left_side) + [pivot] + quickSort(right_side)

# 계수 정렬
def countSort(array):
    # 0으로 채워진 array의 최대값의 크기를 배열을 구함
    # 이 배열을 활용해 값이 존재하는지 카운트 할 예정
    count = [0] * (max(array) + 1)

    # array 배열의 인덱스를 반환
    for i in range(len(array)):
        # array 배열 속에서 뽑은 값을 count 배열에 +1을 함
        # ex) 2가 나왔다면
        # count = [0,0,1] 이렇게 바뀜
        count[array[i]] += 1

    # count 배열의 인덱스이자 카운트 배열 속에 존재하는 값
    for i in range(len(count)):
        # 카운트 배열 속에 존재하는 값의 카운트의 수를 구함
        # ex) count = [0, 0, 1] 이라면
        # 그 값은 2가 나옴
        for j in range(count[i]):
            print(i, end=' ')

array = [7,5,9,0,0,3,1,6,4,7,8]

print(selectionSort(array))
print(insertionSort(array))
print(quickSort(array))
countSort(array)