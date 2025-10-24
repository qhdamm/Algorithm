from collections import Counter
def solution(clothes):
    hclothes = Counter(cate for _, cate in clothes)
    ans =1
    for n in hclothes.values():
        ans *= (n+1)
    return ans -1
    
