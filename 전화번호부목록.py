# def solution(phone_book):
#     head = str(phone_book[0])
#     phone_book=str(phone_book)
#     answer = phone_book.startswith(head)
#     return answer

# print(solution(["119", "97674223", "1195524421"]))

# print(solution(["123","456","789"]))

def solution(phone_book):
    head = phone_book[0]
    headstart = []

    if len(phone_book) == 1:
        return False

    for i in range(1, len(phone_book)):
        headstart.append(phone_book[i].startswith(head))
    print(headstart)
    if True in headstart:
        return False
    else:
        return True

print(solution(["123","456","789"]))
print(solution(["119", "97674223", "1195524421"]))
print(solution(["12","123","1235","567","88"]))