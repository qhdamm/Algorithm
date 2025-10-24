from collections import Counter

def solution(participant, completion):
    c_par = Counter(participant)
    c_com = Counter(completion)
    ans = c_par - c_com
    answer = list(ans.keys())[0]
    return answer