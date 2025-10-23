def solution(citations):
    citations.sort()  # [0,1,3,5,6]
    n = len(citations)
    for i in range(n):
        h = n-i
        if citations[i] >= h:
            return h
    return 0