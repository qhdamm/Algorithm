## 시간 초과
# n = int(input())

# n_list = []
# for i in range(n):
#     n_list.append(i+1)

# def drop_top(n_list):
#     return n_list[1:]

# def switch_cards(n_list):
#     new_list = n_list[1:]
#     new_list.append(n_list[0])
#     return new_list

# while len(n_list) > 1:
#     n_list = drop_top(n_list)
#     n_list = switch_cards(n_list)

# print(*n_list)

from collections import deque

n = int(input())
n_deque = deque(range(1, n+1))


while len(n_deque)>1:
    n_deque.popleft()
    n_deque.append(n_deque.popleft())
print(n_deque[0])