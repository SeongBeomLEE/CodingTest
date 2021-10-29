# 베스트앨범
# 지하철에서 핸드폰으로 코딩함ㅎㅎ
def solution(genres, plays):
    dic = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic:
            dic[genre] = [play,[(play, idx)]]
        else:
            dic[genre][0] += play
            dic[genre][1] += [(play, idx)]
    val = sorted(list(dic.values()), reverse = True)
    answer = []
    for total, ans_li in val:
        for play, idx in sorted(ans_li, reverse = True, key = lambda x : (x[0], -x[1]))[:2]:
            answer += [idx]
    return answer
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))