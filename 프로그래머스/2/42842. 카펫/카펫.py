def solution(brown, yellow):
    answer = []
    if yellow == 1:
        answer = [3, 3]
    for i in range(1, yellow//2 + 1):
        if yellow % i == 0:
            yellow_y = i; brown_y = yellow_y + 2
            yellow_x = yellow // i; brown_x = yellow_x + 2
            if brown_x * brown_y == (brown+yellow):
                answer.append(brown_x); answer.append(brown_y)
                break
    
    return answer