T = int(input())
for i in range(T):
    N, C = input().split()
    text =""
    for i in C:
        text += int(N)*i
    print(text)