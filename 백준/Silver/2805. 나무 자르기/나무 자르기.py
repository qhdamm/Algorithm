import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))
tree_list.sort()
start = 0
end = max(tree_list)
result = 0


def get_wood(cut):
    return sum((tree-cut) for tree in tree_list if tree>cut)
        
while start <= end:
    med = (start+end) // 2
    wood = get_wood(med)
    
    if wood >= M:
        start = med + 1
        result = med
    else:
        end = med - 1

print(result)
