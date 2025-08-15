def solution(n, times):
    times.sort()
    min_time = 0
    max_time = n*times[-1]
    answer = max_time
    
    while min_time <= max_time:
        mid = (min_time + max_time) // 2
        if entry(mid, times) >= n:
            answer = mid
            max_time = mid-1
        else:
            min_time = mid+1
    return answer

# 어떤 시간 t 동안 몇 명이 심사를 받을 수 있는지 알려주는 함수
def entry(t, times):
    people = 0
    for i in times:
        people += (t // i)
        
    return people