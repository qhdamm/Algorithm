from itertools import product
def solution(word):
    a_list = ['A', 'E', 'I', 'O', 'U']
    make_word = []
    for i in range(1, 6):
        for w in product(a_list, repeat=i):
            make_word.append("".join(w))
    make_word.sort()
    answer = make_word.index(word) + 1
    
    return answer