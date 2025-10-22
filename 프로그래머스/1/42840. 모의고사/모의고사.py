def solution(answers):
    n = len(answers)
    sol1 = []
    sol2 = []
    sol3 = []
    while len(sol1) < n:
        for i in range(1, 6):
            sol1.append(i)
    while len(sol2) < n:
        for i in [1, 3, 4, 5]:
            sol2.append(2)
            sol2.append(i)
    while len(sol3) < n:
        for i in [3, 1, 2, 4, 5]:
            sol3.append(i)
            sol3.append(i)
    
    ans1 = ans2 = ans3 = 0
    for i, a in enumerate(answers):
        if sol1[i] == a:
            ans1 += 1
        if sol2[i] == a:
            ans2 += 1
        if sol3[i] == a:
            ans3 += 1
    max_sol = max(ans1, ans2, ans3)
    answer = []
    
    if ans1 == max_sol:
        answer.append(1)
    if ans2 == max_sol:
        answer.append(2)
    if ans3 == max_sol:
        answer.append(3)
    answer.sort()
    
    return answer