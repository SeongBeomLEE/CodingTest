T = int(input())
for _ in range(T):
    s = input()
    for i in range(1,len(s)):
        # 뒤에 단어의 인덱스가 앞에 단어의 인덱스보다 크다면
        # 앞에 단어는 한번 나왔던 단어이므로 그룹 단어가 아님
        # 뒤에 단어         앞에 단어
        if s.find(s[i-1]) > s.find(s[i]):
            T -= 1
            break
print(T)