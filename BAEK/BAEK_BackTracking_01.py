import itertools
def soliution(N, M):
    numbers = [i for i in range(1, N+1)]
    li = list(map(list, itertools.permutations(numbers, M)))
    for i in li:
        for j in i:
            print(j, end=' ')
        print()
N, M = map(int, input().split())
soliution(N, M)