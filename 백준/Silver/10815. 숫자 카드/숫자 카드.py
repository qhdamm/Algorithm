import sys
input = sys.stdin.readline
N = int(input())
sang_list = list(map(int, input().split()))
sang_list.sort()
M = int(input())
card_list = list(map(int, input().split()))

# card에 대해 상근이가 가지고 있는지 판단하는 함수
def decision(card_num):
    start = 0
    end = len(sang_list) - 1
    
    while start <= end:
        mid = (start+end) // 2
        if sang_list[mid] == card_num:
            return 1
        elif card_num < sang_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 0

answer = [decision(card) for card in card_list]
print(' '.join(map(str, answer)))