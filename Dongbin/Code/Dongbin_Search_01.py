# 순차 탐색
def sequential_search(n, target, array):
    '''
    :param n: 찾고자 하는 배열의 크기
    :param target: 찾고자 하는 값
    :param array: 찾고자 하는 값이 들어있는 정렬된 배열
    :return: 찾고자 하는 값이 들어있는 위치
    '''
    # 각 원소를 하나씩 확인
    for i in range(n):
        if array[i] == target:
            return i + 1

    # 값이 존재하지 않으면 None 반환
    return None

# 이진 탐색
def binary_search(array, target, start, end):
    '''
    :param array: 찾고자 하는 값이 들어있는 정렬된 배열
    :param target: 찾고자 하는 값
    :param start: 제일 처음의 인덱스
    :param end: 제일 마지막의 인덱스
    :return: 찾고자 하는 값이 들어있는 위치
    '''
    # 탐색할 배열의 끝값이 시작값보다 커지면 멈춤
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        # 타겟 중간값 순으로 존재하므로 왼쪽 탐색
        elif array[mid] > target:
            end = mid - 1
        # 중간값 타겟 순으로 존재하므로 오른쪽 탐색
        else:
            start = mid + 1
    # 값이 존재하지 않음
    return None