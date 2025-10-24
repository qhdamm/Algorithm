def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        n = len(phone_book[i])
        if len(phone_book[i+1]) >= n and phone_book[i+1][:n] == phone_book[i]:
            answer = False
            return answer
        
    return answer