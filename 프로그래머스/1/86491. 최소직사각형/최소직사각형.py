def solution(sizes):
    max_x = 0
    max_y = 0
    
    for size in sizes:
        if size[0] >= size[1]:
            max_x = max(max_x, size[0])
            max_y = max(max_y, size[1])
        else:
            max_x = max(max_x, size[1])
            max_y = max(max_y, size[0])
            
            
        
    answer = max_x * max_y
    return answer