def solution(genres, plays):
    answer = []
    playlist = {}
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in playlist:
            playlist[genre] = [play, [(play, idx)]]
        else:
            playlist[genre][0] += play
            playlist[genre][1] += [(play, idx)]

    val = list(playlist.values())
    val.sort(key=lambda x: (x[0]), reverse=True)
    for v in val:
        total_cnt, play_and_idx = v
        play_and_idx = sorted(play_and_idx, key=lambda x: (-x[0], x[1]))
        for play, idx in play_and_idx[:2]:
            answer += [idx]

    return answer