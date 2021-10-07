# 전화번호 목록
def solution(phone_book):
    answer = True
    phone_book.sort()
    for idx, phone_number in enumerate(phone_book[:-1]):
        len_phone_number = len(phone_number)
        if phone_number == phone_book[idx + 1][:len_phone_number]:
            answer = False
            break
    return answer
phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123","456","789"]
# phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))