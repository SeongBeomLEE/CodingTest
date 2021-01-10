char = input().upper()
char_count = []
for i in set(char):
    char_count.append(char.count(i))

index = [idx for idx, i in enumerate(char_count) if i == max(char_count)]

if len(index) > 1:
    print("?")
else:
    print(list(set(char))[index[0]])
