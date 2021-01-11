# 성적이 낮은 순서로 학생 출력하기
array = []
for _ in range(int(input())):
    data = input().split()
    array.append((data[0], int(data[1])))

array.sort(key= lambda x : x[1])
for v in array:
    print(v[0], end=' ')




