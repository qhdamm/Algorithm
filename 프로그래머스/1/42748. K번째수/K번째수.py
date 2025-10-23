def solution(array, commands):
    answer = []
    for command in commands:
        s_arr = array[command[0]-1:command[1]]
        s_arr.sort()
        answer.append(s_arr[command[2]-1])
    return answer