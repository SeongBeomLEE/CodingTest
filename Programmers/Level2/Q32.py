# 파일명 정렬
import re
def solution(files):
    answer = []
    for idx, file in enumerate(files):
        head = re.sub('[0-9]', '#', file).split('#')[0].lower()
        tail = int(re.sub('[^0-9]', '#', file[len(head):]).split('#')[0])
        answer.append([head, tail, idx])
    return [files[idx] for h, t, idx in sorted(answer)]

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))