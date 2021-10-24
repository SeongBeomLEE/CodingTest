# 단어 뒤집기
def solve(words):
    answer = []
    for word in words:
        word = word.split(' ')
        a = []
        for w in word:
            new_word = []
            for _w in w[::-1]:
                new_word.append(_w)
            a.append("".join(new_word))

        answer.append(" ".join(a))

    return answer

words = []
for _ in range(int(input())):
    words.append(input())
for w in solve(words):
    print(w)

