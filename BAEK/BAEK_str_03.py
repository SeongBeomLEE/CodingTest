import string
char = input()

all_char = string.ascii_lowercase
all_char_list = { i : -1 for i in all_char}
char_index = {}
for idx, c in enumerate(char):
    if c in char_index.keys():
        continue
    else:
        char_index[c] = idx

for i in char:
    all_char_list[i] = char_index[i]

for i in all_char:
    print(all_char_list[i] , end=" ")