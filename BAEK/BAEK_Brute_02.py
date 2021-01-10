N = int(input())
N_list = [i for i in range(0,N)]
ret = []
for n in N_list:
    if sum([n] + list(map(int, list(str(n))))) == N:
        ret.append(n)
if len(ret) == 0: print(0)
else: print(min(ret))