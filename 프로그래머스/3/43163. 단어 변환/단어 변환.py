from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    def is_one_change(word, next_word):
        # 두 개의 단어 중 한 글자만 바꼈는지 판단
        change = 0
        list1 = list(word)
        list2 = list(next_word)
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                change += 1
        if change == 1:
            return True
        return False
    
    visited = {}
    for w in words:
        visited[w] = -1
        
    def bfs(word): # hit
        q = deque() 
        q.append(word)
        visited[word] = 0
        while q:
            word = q.popleft()
            for w in words:
                if is_one_change(word, w) and visited[w] == -1:
                    q.append(w)
                    visited[w] = visited[word] + 1
    
    bfs(begin)
    return visited[target]