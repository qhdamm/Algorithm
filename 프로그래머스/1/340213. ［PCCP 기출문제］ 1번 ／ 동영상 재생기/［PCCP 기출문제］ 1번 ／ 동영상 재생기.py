def solution(video_len, pos, op_start, op_end, commands):
    # pos: 기능 직전의 재생위치
    now_int = time2int(pos)
    op_start_int = time2int(op_start)
    op_end_int = time2int(op_end)
    video_int = time2int(video_len)
    for command in commands:
        if op_start_int <= now_int <= op_end_int:
            now_int = skipop(now_int, op_end_int)
        if command=="prev":
            now_int = move2prev(now_int)
        if command=="next":
            now_int = move2next(now_int, video_int)
        if op_start_int <= now_int <= op_end_int:
            now_int = skipop(now_int, op_end_int)
    
    mm = str(now_int // 60)
    ss = str(now_int % 60)
    answer = f'{mm.zfill(2)}:{ss.zfill(2)}'  #"mm:ss" 형식
    return answer

def time2int(time) -> int:
    mm, ss = time.split(":")
    mm = int(mm)
    ss = int(ss)
    return 60*mm + ss

def move2prev(time_int):
    if time_int > 10:
        now_int = time_int - 10
    else:
        now_int = 0
    return now_int

def move2next(time_int, video_int): 
    if time_int + 10 > video_int:
        now_int = video_int
    else:
        now_int = time_int + 10
    return now_int

def skipop(now_int, op_end_int):  #pos가 오프닝인경우 자동 스킵
    return op_end_int